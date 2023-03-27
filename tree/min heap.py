def heapify(arr,n,i):
    smallest = i
    l = 2*i +1
    r = 2*i +2
    
    if l < n and arr[i] > arr[l]:
        smallest = l
    if r < n and arr[smallest] > arr[r]:
        smallest = r
    if smallest != i :
        arr[i],arr[smallest] = arr[smallest],arr[i]
        heapify(arr,n,smallest)
        
        
def insert(array):
    size = len(array)
    for i in range((size//2)-1, -1, -1):
        heapify(array, size, i)
            
            
def deletenode(array,num):
    size = len(array)
    for i in range(0,size):
        if num == array[i]:
            break
    array[i],array[size-1] = array[size-1],array[i]
    array.remove(num)
    for i in range((size//2)-1,-1,-1):
        heapify(array,len(array),i)
        

arr= [10,2,3,45,7,9,11]
insert(arr)
print("Min-Heap array: ",str(arr))

deletenode(arr,2)
print("\n\nAfter deletion: ",str(arr))