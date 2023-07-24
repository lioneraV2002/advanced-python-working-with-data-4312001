# Demonstrate the usage of namedtuple objects

import collections

# like dictionaries, the contain keys that are hashed to a particular value.
# But on contrary, it supports both access from key-value and iteration,
# the functionality that dictionaries lack.
# with namedtuple, you can create immutable sequence types
# that allow you to access their values using descriptive field names
# and the dot notation instead of unclear integer indices.

# TODO: create a Point namedtuple

Point = collections.namedtuple('Point', "x y")

p1 = Point(10, 30)
p2 = Point(30, 40)

# TODO: use _replace to create a new instance
p3 = p1._replace(x=100)
print(p3)
