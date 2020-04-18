from collections import defaultdict

number = str(input())

digits_frequency = defaultdict(int)

for digit in number:
    digits_frequency[digit] += 1

print(digits_frequency)
