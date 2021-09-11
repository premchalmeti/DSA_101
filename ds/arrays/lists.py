from functools import reduce


# 1. Create:
nos = list(range(10))
chars = list('Premkumar')

# 2. Read: iterate: loops, filter, map, reduce
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
i = chars.index(ch)
print(f"Index of {ch} is {i}", chars)

rep = 'm'
chars[i] = rep
print(f"Replaced {ch} with {rep}", chars)

del chars[i]
print(f"Deleted {i}th char which was {rep}", chars)

ch = 'a'
chars.remove(ch)
print(f'Removed {ch}', chars)

ch = chars.pop() # last char also accepts index to pop out
print(f'Popped {ch}')
