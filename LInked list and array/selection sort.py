def selection_sort(arr,size):
	for ind in range(size):
		min_index=ind
		for j in range (ind+1,size):
			if arr[j]< arr[min_index]:
				min_index=j
		arr[ind],arr[min_index]=arr[min_index],arr[ind]
arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(arr)
selection_sort(arr, size)
print(arr)