import requests
import xml.etree.ElementTree as ET
from services.models import DepartureTime
from services.models import Location
from django.core.cache import cache
import datetime

locationCache = {}

def getDepartureTime(queryParams):
	# user's location is in queryParams
    if 'u1' in queryParams:
        print (queryParams['u1'])
    if 'u2' in queryParams:
        print (queryParams['u2'])

    # here we hard coded stop code 10 and 12
    result = getDepartureTimeByStopCode(10)
    result.extend(getDepartureTimeByStopCode(12))
    
    return result


def getDepartureTimeByStopCode(stopCode):
	now = datetime.datetime.now()

	# Step 1
	# try to get departure time from cache
	if stopCode in cache:
		cachedResult = cache.get(stopCode)

		newResult = []
		for dt in cachedResult:
			nextDepartureTime = dt.nextDepartureTime - (now - dt.created).seconds / 60
			if nextDepartureTime <= 0 :
				break
			newdt = DepartureTime(agencyName=dt.agencyName, routeName=dt.routeName, stopName=dt.stopName, stopCode=dt.stopCode, nextDepartureTime=nextDepartureTime)
			newdt.latitude = dt.latitude
			newdt.longitude = dt.longitude
			newResult.append(newdt)

		if (len(newResult) == len(cachedResult)):
			return newResult

	#
	# Cache miss, and make a service call to get the departure time
	#
	r = requests.get('http://services.my511.org/Transit2.0/GetNextDeparturesByStopCode.aspx?token=8c1a4416-8748-493a-8da4-e632c6c41647&stopcode=' + str(stopCode))
	if r.status_code != 200:
		return []

	tree = ET.fromstring(r.text)
	result = []

	if len(tree) <= 0 or len(tree[0]) <= 0:
		return result

	minTime = 600
	for agency in tree[0]:
		# currently we only support BART
		agencyName = agency.attrib['Name']
		if agencyName != 'BART':
			continue

		# print agency.tag
		for routelist in agency:
			for route in routelist:
				routeName = route.attrib['Name']
				if len(route) >= 1 and len(route[0]) >= 1 and len(route[0][0]) >=1 and len(route[0][0][0]) >= 1:
					stopName = route[0][0].attrib['name']
					stopCode = route[0][0].attrib['StopCode']
					next = int(route[0][0][0][0].text)
					if next * 60 > minTime:
						nimTime = next * 60
					dt = DepartureTime(created=now, agencyName=agencyName, routeName=routeName, stopName=stopName, stopCode=stopCode, nextDepartureTime=next)
					loc = getLocation(int(stopCode))

					print (stopCode)

					# add if only we have a valid location associated
					if loc[0] != -1 and loc[1] != -1:
						dt.latitude = loc[0]
						dt.longitude = loc[1]
						result.append(dt)

	if stopCode not in cache:
		if (len(result) > 0):
			cache.set(stopCode, result, minTime)

	return result

def getLocation(stopCode):
	global locationCache
	if len(locationCache) == 0:
		newCache = {}
		locall = Location.objects.all()
		for loc in locall:
			newCache[loc.stopCode] = (loc.latitude, loc.longitude)

		if (len(locationCache) == 0):
			locationCache = newCache

	if stopCode in locationCache:
		return locationCache[stopCode]
	else:
		return (-1, -1)

