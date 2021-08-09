import unittest
from datetime import date, timedelta

from src.product import Product


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.past = date.today() - timedelta(days=5)
        self.future = date.today() + timedelta(days=5)
        self.product = Product(name='egg', volume=1, expiration_date=self.future, freezable=True)

    def test_create_product(self):
        self.assertIsInstance(self.product, Product)
        self.assertEqual(str(self.product), 'egg')

    def test_product_volume_is_int_or_float(self):
        self.assertIsInstance(self.product.volume, (int, float))

    def test_product_volume_is_not_int_or_float(self):
        with self.assertRaises(TypeError) as context:
            Product(name='egg', volume='a', expiration_date=self.future, freezable=True)

        self.assertTrue('Volume has incorrect type a.' in str(context.exception))

    def test_product_expiration_date_is_one_day_ahead_today(self):
        tomorrow = date.today() + timedelta(days=1)
        self.assertGreaterEqual(self.product.expiration_date, tomorrow)

    def test_product_expiration_date_is_one_day_before_today(self):
        with self.assertRaises(ValueError) as context:
            self.product.expiration_date = self.past

        self.assertTrue('Product is outdated.' in str(context.exception))
