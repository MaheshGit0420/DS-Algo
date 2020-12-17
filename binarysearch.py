# BinarySearch Iterative

# def binary_search(item_list,item):
# 	first = 0
# 	last = len(item_list)-1
# 	found = False
# 	while( first<=last and not found):
# 		mid = (first + last)//2
# 		if item_list[mid] == item :
# 			found = True
# 		else:
# 			if item < item_list[mid]:
# 				last = mid - 1
# 			else:
# 				first = mid + 1	
# 	return found
	
# print(binary_search([1,2,3,5,8], 6))
# print(binary_search([1,2,3,5,8], 5))

#BinarySearch Recursive
def binarysearch(arr_list, low, high, key):
	if low <= high:
		mid = (low+high) // 2
		try:
			if arr_list[mid] == key:
				print(f'{key} is found at the position {mid}')
		except IndexError as e:
			print(f'{key} is not found')
		else:
			if arr_list[mid] > key:
				return binarysearch(arr_list, low, mid-1, key)
			else:
				return binarysearch(arr_list, mid+1, high, key)
	else:
		return False

binarysearch([1,2,3,4,5,6,7,8,9], 0, 9, 12)