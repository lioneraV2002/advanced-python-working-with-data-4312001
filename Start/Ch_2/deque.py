# deque objects are like double-ended queues

import collections
import string

# TODO: initialize a deque with lowercase letters
d = collections.deque(string.ascii_lowercase)

# TODO: deques support the len() function

print("Item count: " + str(len(d)))

# TODO: deques can be iterated over
for elements in d:
    print(elements.upper())

# TODO: manipulate items from either end
# pop value from rightmost position
d.pop()
# pop value from left
d.popleft()
# append value to the rightmost position
d.append(2)
# append to the left side
d.appendleft(12)
print(d)

# TODO: use an index to get a particular item
print(d)
# rotate the deque to right, if negative, rotate left
d.rotate(1)
print(d)
print(d[1])
d.rotate(-3)
print(d)
