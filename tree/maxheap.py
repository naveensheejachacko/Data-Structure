def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2 
    if l < n and arr[i] < arr[l]:
        largest = l 
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr, n, largest)
        
def insert(array):
    size = len(array)
    for i in range((size//2)-1, -1, -1):
        heapify(array, size, i)
        
def deleteNode(array, num):
    for i in range(0, len(array)):
        if num == array[i]:
            break    
    if num not in array:
        print("node not found")
        return
    array[i], array[len(array)-1] = array[len(array)-1], array[i]
    array.remove(num)
    for i in range((len(array)//2)-1, -1, -1):
        heapify(array, len(array), i)
arr= [1, 5, 10, 15, 17, 20, 30]
insert(arr)

print ("Max-Heap array: " ,str(arr))
deleteNode(arr, 22)
print('After deleting:',str(arr))