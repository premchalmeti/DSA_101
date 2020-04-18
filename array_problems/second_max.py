

def get_second_max_no(arr):
	f, s = float('-inf'), float('-inf')

	for n in arr:
		if n > f:
			s = f
			f = n
		elif n > s and n != f:
			s = n

	return s


if __name__ == '__main__':
	arr = [1, 2, 3, 4, 8, 7]
	print get_second_max_no(arr)
