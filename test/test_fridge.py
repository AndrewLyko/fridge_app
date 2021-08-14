import unittest

from src.fridge import Fridge


class TestFridge(unittest.TestCase):
    def setUp(self):
        self.fridge = Fridge(cooler_volume=250, freezer_volume=100)

    def test_create_fridge(self):
        self.assertIsInstance(self.fridge, Fridge)
        self.assertEqual(str(self.fridge), "Cooler Volume: 250l, freezer volume: 100l")

    def test_if_cooler_volume_is_not_negative(self):
        self.fridge.cooler_volume = -50
        self.assertEqual(250, self.fridge.cooler_volume)

    def test_if_freeze_volume_is_not_negative(self):
        self.fridge.freezer_volume = -50
        self.assertEqual(100, self.fridge.freezer_volume)
