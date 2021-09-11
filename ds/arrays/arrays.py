# Python supports arrays (homogenous) DS
# https://docs.python.org/3/library/array.html

from array import array
from functools import reduce


# 1. Create: Array takes typecode
chars = array('b')
chars.fromlist(list(map(ord, list("Premkumar"))))

nos = array('i')
nos.fromlist(list(range(10)))


# 2. Read
print('Number array', nos)
print("Character array", chars)
print("Joined string", ", ".join(list(map(str, chars))))

evens = [n for n in nos if n % 2 == 0]
print("Even nos", evens)

sqaures = list(map(lambda n: n * n, evens))
print("Square of evens", sqaures)

odds = list(filter(lambda n: n % 2 != 0, nos))
print("Odd nos", odds)

sum = reduce(lambda acc, n: acc+n, odds)
print("Sum of odd nos", sum)


# 3. Update
ch = 'k'
i = chars.index(ord(ch))
print(f"Index of {ch} is {i}", chars)

rep = 'm'
chars[i] = ord(rep)
print(f"Replaced {ch} with {rep}", chars)

del chars[i]
print(f"Deleted {i}th char which was {rep}", chars)

ch = ord('a')
chars.remove(ch)
print(f'Removed {chr(ch)}', chars)

ch = chars.pop() # last char also accepts index to pop out
print(f'Popped {chr(ch)}')
