def linearsearch(item_list, key):
	for i in range(len(item_list)):
		if item_list[i] == key:
			print(f'{key} is found at {i}')


linearsearch([1,2,3,4,5,6,7,8,9],7)
