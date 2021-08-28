
def check_validity(expr):
	stack = []

	for c in expr:
		if c in ['(', '[', '{']:
			stack.append(c)
		elif c in [')', ']', '}']:
			if not stack:
				return False

			b = stack.pop()

			if c == ')' and b != '(' or c == ']' and b != '[' or c == '}' and b!= '{':
				return False

	return True if not stack else False


if __name__ == '__main__':
	print(check_validity('([()])'))
