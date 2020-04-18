from __future__ import print_function
from functools import reduce

numbers = [1, 2, 3, 4]

# list comprehension

even_nos = [no for no in numbers if no % 2 == 0]

# because in python3 filter, map returns views
odd_nos = list(filter(lambda no: no % 2 != 0, numbers))

square_nos = list(map(lambda no: no ** 2, even_nos))

# in python3 reduce is no longer built-in function
sum_of_all = reduce(lambda acc, no: acc+no, numbers)

print(even_nos, odd_nos, square_nos, sum_of_all)

