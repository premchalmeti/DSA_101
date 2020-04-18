
def print_mat(N, M):
	up = [(".|."*(2*i+1)).center(M, '-') for i in range(N//2)]

	mid = ['WELCOME'.center(M, '-')]

	low = up[::-1]

	print('\n'.join(up+mid+low))

if __name__ == '__main__':
	N, M = map(int, input("Enter N M:").split())
	# N, M = 7, 21
	print_mat(N, M)
