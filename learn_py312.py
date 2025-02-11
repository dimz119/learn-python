# from math import pi

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return pi * radius**2

# Circle(5).area()

# Traceback (most recent call last):
#   File "/Users/seungjoonlee/git/learn-python/learn_py312.py", line 10, in <module>
#     Circle(5).area()
#   File "/Users/seungjoonlee/git/learn-python/learn_py312.py", line 8, in area
#     return pi * radius**2
#                 ^^^^^^
# NameError: name 'radius' is not defined. Did you mean: 'self.radius'?

# >>> version = {"major": 3, "minor": 12}
# >>> f"Python {version["major"]}.{version["minor"]}"
# 'Python 3.12'

# >>> names = ["Seoul", "Incheon", "Busan"]
# >>> print(f"Cities:\n {"\n ".join(names)}")
# Cities:
#  Seoul
#  Incheon
#  Busan

# >>> print(f"Cities: {
# ...     ", ".join(names) # join cities
# ... }")
# Cities: Seoul, Incheon, Busan

# type Person = tuple[str, int]
# type ListOrSet[T] = list[T] | set[T]
# type IntegerList = list[int]

# # Now you can use IntegerList as a type annotation
# def process_numbers(numbers: IntegerList) -> int:
#     total = sum(numbers)
#     return total


# >>> import sys
# >>> a = 3.12
# >>> sys.getrefcount(a)
# 2
# >>> b = a
# >>> sys.getrefcount(a)
# 3
# >>> del b
# >>> sys.getrefcount(a)
# 2
# >>> sys.getrefcount(None)
# 4294967295
# >>> a = None
# >>> sys.getrefcount(None)
# 4294967295
# >>> sys.getrefcount(True)
# 4294967295
# >>> c = True
# >>> sys.getrefcount(True)
# 4294967295

# names = ["Seoul", "Incheon", "Busan"]
# >>> [name[::-1].title() for name in names]


# from typing import override

# class Base:
#   def get_color(self) -> str:
#     return "blue"

# class GoodChild(Base):
#   @override  # ok: overrides Base.get_color
#   def get_color(self) -> str:
#     return "yellow"

# class BadChild(Base):
#   @override  # type checker error: does not override Base.get_color
#   def get_colour(self) -> str:
#     return "red"