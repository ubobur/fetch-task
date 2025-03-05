import unittest
from geoloc_util import get_location_info

class TestGeoLocUtil(unittest.TestCase):

    def test_city_state(self):
        result = get_location_info("Madison, WI")
        self.assertEqual(result["name"], "Madison")
        self.assertEqual(result["state"], "Wisconsin")
        self.assertEqual(result["country"], "US")
        self.assertAlmostEqual(result["lat"], 43.0731, places=2)
        self.assertAlmostEqual(result["lon"], -89.3837, places=2)

    def test_zip_code(self):
        result = get_location_info("10001")
        self.assertEqual(result["name"], "New York")
        self.assertEqual(result["country"], "US")
        self.assertAlmostEqual(result["lat"], 40.7501, places=2)
        self.assertAlmostEqual(result["lon"], -73.9972, places=2)
        self.assertEqual(result["zip"], "10001")

    def test_invalid_location(self):
        result = get_location_info("InvalidCity, XX")
        self.assertEqual(result, {})

    def test_invalid_zip(self):
        result = get_location_info("00000")
        self.assertEqual(result, {})

if __name__ == "__main__":
    unittest.main()
