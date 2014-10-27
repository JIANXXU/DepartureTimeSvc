import requests
import xml.etree.ElementTree as ET
from services.models import DepartureTime
from services.models import Location

locationCache = {}

def getDepartureTime(stopCode):
	r = requests.get('http://services.my511.org/Transit2.0/GetNextDeparturesByStopCode.aspx?token=8c1a4416-8748-493a-8da4-e632c6c41647&stopcode=' + str(stopCode))
	if r.status_code != 200:
		return []

	tree = ET.fromstring(r.text)
	result = []

	if len(tree) <= 0 or len(tree[0]) <= 0:
		return result

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
					dt = DepartureTime(agencyName=agencyName, routeName=routeName, stopName=stopName, stopCode=stopCode, nextDepartureTime=next)
					loc = getLocation(int(stopCode))

					# add if only we have a valid location associated
					if loc[0] != -1 and loc[1] != -1:
						dt.latitude = loc[0]
						dt.longitude = loc[1]
						result.append(dt)

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

