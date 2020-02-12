"""Task 3"""

from itertools import zip_longest

FIRST_LIST = [1, 2, 3, 4, 5]
SECOND_LIST = ['one', 'two', 'three', 'four']
NEW_DICT = {x: y for x, y in zip_longest(FIRST_LIST, SECOND_LIST) if x is not None}
print(NEW_DICT)
