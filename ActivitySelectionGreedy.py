# Sorting the jobs with respect to finishing time
def sort_nestedArrBy_index(arr):
	l = len(arr)
	for i in range(0, l):
		for j in range(0, l-i-1):
			if (arr[j][2] > arr[j+1][2]):
				temp = arr[j][2]
				arr[j][2] = arr[j+1][2]
				arr[j+1][2] = temp
	return arr



# Selecting optimal jobs from sorted jobs
def ActivitySelection(arr):
	sorted_arr = sort_nestedArrBy_index(arr)
	jobs = [sorted_arr[0]]
	for job in range(1,len(sorted_arr)):
		if sorted_arr[job][1] >= jobs[-1][2]:
			jobs.append(sorted_arr[job])
	return jobs

print(ActivitySelection([[1,12, 25], [2, 10, 20], [3, 20, 30]]))
