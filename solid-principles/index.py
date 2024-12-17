from enum import Enum
from abc import ABC, abstractmethod
from typing import List

# The solid design principles

# Single Responsibility Principle

'''
A class should have the primary responsibility what it's ment to take, not other than that.
'''

# Journal main logic is to add or remove journal
class Journal:
  def __init__(self):
    self.entries = []
    self.count = 0

  def add_entries(self, text):
    self.count += 1
    self.entries.append(f'{self.count}: {text}')

  def remove_entries(self, pos):
    del self.entries[pos - 1]

  def __str__(self):
    return '\n'.join(self.entries)
  
# Save and load files
class PersistanceManager:
  @staticmethod
  def save_to_file(journal, filename):
    file = open(filename, 'w')
    file.write(str(journal))
    file.close()

journal = Journal()
journal.add_entries('I cried today.')
journal.add_entries('I ate a bug.')
journal.add_entries('I won grammy.')
# print(f'Journal entries: \n{journal}')
journal.remove_entries(3)
# print(f'Journal entries: \n{journal}')

# Open Close Principle

'''
When you add new functionality you add it via extension not via modifications.
Open for extension, close for modification.
'''

class Color(Enum):
  RED = 1
  GREEN = 2
  BLUE = 3

class Size(Enum):
  SMALL = 1
  MEDIUM = 2
  LARGE = 3

class Product:
  def __init__(self, name: str, color: Color, size: Size, price: float):
    self.name = name
    self.color = color
    self.size = size
    self.price = price

class Specification(ABC):
  @abstractmethod
  def is_satisfied(self, item: Product) -> bool:
    pass

  def __and__(self, other):
    return AndSpecification(self, other)

class Filter(ABC):
  @abstractmethod
  def filter(self, items: List[Product], spec: Specification) -> List[Product]:
    pass

class ColorSpecification(Specification):
  def __init__(self, color: Color):
    self.color = color

  def is_satisfied(self, item: Product) -> bool:
    return item.color == self.color

class SizeSpecification(Specification):
  def __init__(self, size: Size):
    self.size = size

  def is_satisfied(self, item: Product) -> bool:
    return item.size == self.size

class PriceSpecification(Specification):
  def __init__(self, min_price: float = None, max_price: float = None):
    self.min_price = min_price
    self.max_price = max_price

  def is_satisfied(self, item: Product) -> bool:
    if self.min_price is not None and item.price < self.min_price:
      return False
    if self.max_price is not None and item.price > self.max_price:
      return False
    return True

# Composite specification for AND logic
class AndSpecification(Specification):
  def __init__(self, *specs: Specification):
    self.specs = specs

  def is_satisfied(self, item: Product) -> bool:
    return all(spec.is_satisfied(item) for spec in self.specs)


# Concrete filter implementation
class ProductFilter(Filter):
  def filter(self, items: List[Product], spec: Specification) -> List[Product]:
    return [item for item in items if spec.is_satisfied(item)]

if __name__ == "__main__":
  apple = Product("Apple", Color.GREEN, Size.SMALL, 10.0)
  tree = Product("Tree", Color.GREEN, Size.LARGE, 20.0)
  house = Product("House", Color.BLUE, Size.LARGE, 100.0)
  car = Product("Car", Color.RED, Size.LARGE, 7000.0)

  products = [apple, tree, house, car]

  pf = ProductFilter()

  green_spec = ColorSpecification(Color.GREEN)
  print("Green products:")
  for p in pf.filter(products, green_spec):
    print(f" - {p.name}")

  red_spec = ColorSpecification(Color.RED)
  print("\nRed Products:")
  for p in pf.filter(products, red_spec):
    print(f" - {p.name}")

  large_spec = SizeSpecification(Size.LARGE)
  print("\nLarge products:")

  for p in pf.filter(products, large_spec):
    print(f" - {p.name}")

  price_spec = PriceSpecification(min_price=50.0, max_price=100.0)
  print("\nProducts priced between $15 and $50:")
  for p in pf.filter(products, price_spec):
    print(f" - {p.name} (${p.price})")

  green_and_price_spec = green_spec & price_spec
  print(f"\nGreen products priced between ${price_spec.min_price} and ${price_spec.max_price}:")
  for p in pf.filter(products, green_and_price_spec):
    print(f" - {p.name} (${p.price})")

  green_large_and_price_spec = green_spec & large_spec & price_spec
  print(f"\nGreen, Large products priced between ${price_spec.min_price} and ${price_spec.max_price}:")
  for p in pf.filter(products, green_large_and_price_spec):
    print(f" - {p.name} (${p.price})")

# Liskov Substitution Principle

'''
It ensures that objects of a superclass can be replaced with objects of a subclass without affecting the functionality of the program.
'''

class Shape(ABC):
  @abstractmethod
  def area(self):
    pass

class Rectangle(Shape):
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def area(self):
    return self.height * self.width
  
class Square(Rectangle):
  def __init__(self, side):
    self.side = side

  def area(self):
    return self.side * self.side

# Interface Segeration Principle

'''
Segregation means keeping things separated, and the Interface Segregation Principle is about separating the interfaces.
'''

# Dependency Inversion Principle

'''
The Dependency Inversion principle states that our classes should depend upon interfaces or abstract classes instead of concrete classes and functions.
'''
