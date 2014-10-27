from django.test import TestCase
from services.application import getLocation, getDepartureTime
from services.models import Location


class testApplication(TestCase):

	def testGetDepartureTIme(self):
		loc = Location(stopCode=12, latitude=37.751992, longitude=-122.418722)
		loc.save()

		times = getDepartureTime(12)
		self.assertEqual(len(times) > 0, True)

	def testValidGetLocation(self):
		locations = getLocation(12)
		self.assertEqual(locations[0] != -1, True)
		self.assertEqual(locations[1] != -1, True)

