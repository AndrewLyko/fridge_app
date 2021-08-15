import unittest
from datetime import date, timedelta

from src.freezer import Freezer
from src.product import Product


class TestFreezer(unittest.TestCase):
    def setUp(self):
        self.freezer = Freezer(250)
        self.future = date.today() + timedelta(days=45)
        self.old = date.today() + timedelta(days=3)

    def test_create_freezer(self):
        self.assertIsInstance(self.freezer, Freezer)
        self.assertEqual(str(self.freezer), 'Freezer has 0 product, free space: 250 l.')

    def test_instance_of_added_product_to_freezer(self):
        with self.assertRaises(TypeError) as context:
            product = Product(name='egg', volume='a', expiration_date=self.future, freezable=True)
            self.freezer.add_products(product)
            Product(name='egg', volume='a', expiration_date=self.future, freezable=True)
            self.assertTrue('egg is not valid type.' in str(context.exception))

    def test_freezable_of_added_product_to_freezer(self):
        with self.assertRaises(TypeError) as context:
            product = Product(name='egg', volume=5, expiration_date=self.future, freezable=False)
            self.freezer.add_products(product)
            Product(name='beer', volume=5, expiration_date=self.future, freezable=False)
            self.assertTrue('beer is not freezable.' in str(context.exception))

    def test_check_of_expiration_date(self):
        product = Product(name='egg', volume=5, expiration_date=self.old, freezable=True)
        self.freezer.add_products(product)
        self.freezer.check_expiration_date()
        self.assertEqual(product, self.freezer.old_products[0])


