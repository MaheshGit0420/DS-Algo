def sort(arr):
	l = len(arr)
	for i in range(0,l-1):
		for j in range(i, l):
			if arr[i] > arr[j]:
				arr[i], arr[j] = arr[j], arr[i]

	return arr

arr = [100,56,102,85,23,11,85,34,89,45,67,34]
print(sort(arr))