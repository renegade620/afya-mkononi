from django.test import TestCase
from .models import Wearable

class WearableModelTest(TestCase):

    def setUp(self):
        Wearable.objects.create(name="Smartwatch", type="Fitness Tracker", battery_life="24 hours")
        Wearable.objects.create(name="Fitness Band", type="Health Monitor", battery_life="7 days")

    def test_wearable_creation(self):
        smartwatch = Wearable.objects.get(name="Smartwatch")
        fitness_band = Wearable.objects.get(name="Fitness Band")
        self.assertEqual(smartwatch.type, "Fitness Tracker")
        self.assertEqual(fitness_band.battery_life, "7 days")

    def test_wearable_str(self):
        wearable = Wearable.objects.get(name="Smartwatch")
        self.assertEqual(str(wearable), "Smartwatch")