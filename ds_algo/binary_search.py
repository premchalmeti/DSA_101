
def binary_search_rec(arr, target, l, h):
	if l > h:
		return -1

	mid = (l+h) // 2

	if arr[mid] == target:
		return mid
	elif arr[mid] > target:
		return binary_search_rec(arr, target, l, mid-1)
	else:
		return binary_search_rec(arr, target, mid+1, h)


def binary_search(arr, target):
	low, high = 0, len(arr)

	while low < high:
		mid = (low+high) // 2

		if arr[mid] == target:
			return mid
		elif arr[mid] > target:
			high = mid-1
		else:
			low = mid+1

	return -1


if __name__ == '__main__':
	arr = [-1, 10, 20, 30, 43, 54, 55, 55, 101]
	target = 10

	result = binary_search_rec(arr, target, 0, len(arr))

	print(result)
