from datetime import date, timedelta
from pprint import pprint as pp

from src.product import Product


class Freezer:
    def __init__(self, volume):
        self.idx = 0
        self.products = []
        self.volume = volume
        self.free_volume = self.check_free_space()
        self.old_products = []

    def add_products(self, product):
        if not isinstance(product, Product):
            raise TypeError(f'{product} is not valid type.')
        if not product.freezable:
            raise TypeError(f'{product} is not freezable.')
        else:
            if product.volume >= self.free_volume:
                raise ValueError(f'Freezer have not enough space to add: {product}.')
        self.products.append(product)
        self.check_free_space()
        self.check_expiration_date()

    def check_expiration_date(self):
        for product in self.products:
            if product.expiration_date <= date.today() + timedelta(days=7):
                self.old_products.append(product)

    def check_free_space(self):
        if len(self.products) > 0:
            space = sum(map(lambda product: product.volume, self.products))
            free_space = int(self.volume) - int(space)
            self.free_volume = free_space
        else:
            return self.volume

    def __len__(self):
        return len(self.products)

    def __str__(self):
        return f"{type(self).__name__} has {len(self.products)} product, free space: {self.free_volume} l."

    def __repr__(self):
        return f'{type(self).__name__}products={self.products}'

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.products):
            raise StopIteration('Stop iteration')
        product = self.products[self.idx]
        self.idx += 1
        return product


p = Product("egg", 5, date.today() + timedelta(days=3), True)
q = Product("beer", 10, date.today() + timedelta(days=4), True)

freezer = Freezer(250)
freezer.add_products(p)
pp(freezer.old_products)
# pprint(str(freezer))
#
# print(len(freezer))
# print(freezer.products)
# print(freezer.free_volume)
