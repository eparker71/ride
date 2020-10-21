from django.test import TestCase
from mbta.utils import getRadius, findMiddleOfCoords
# Create your tests here.

class UtilsTestCase(TestCase):
    def setUp(self):
        pass
    
    def test_get_radius_returns_correct_result(self):
        # """Testing """
        coords = [(42.39674, -71.121815), (42.390067, -71.107802), (42.394225, -71.080798)]
        center = (42.38686, -71.080685)
        raduis = getRadius(coords, center)
        self.assertEqual(raduis, 2.2070503102282975)
    
    def test_find_middle_of_coords(self):
        coords = [(10.45, 2.78),
                  (3.92, 8.67)]
        center = findMiddleOfCoords(coords)
        self.assertEqual(center, (7.185, 5.725))
