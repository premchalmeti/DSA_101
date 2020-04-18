
def print_rangoli(size):
	import string
	alphas = string.ascii_lowercase

	f_half = []
	# max mid line
	col = 4 * size - 3

	for r in range(size):
		mid_left_chars = alphas[:r]
		line = "-".join(mid_left_chars + alphas[size-1] + mid_left_chars[::-1])
		f_half.append(line.center(col, '-'))

	# exclude mid_line after reverse
	print('\n'.join(f_half+f_half[size-1-1::-1]))


if __name__ == '__main__':
    n = 7
    print_rangoli(n)
