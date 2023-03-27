def heapify(array,size,i):
    largest=i
    l=2*i+1
    r=2*i+2
    if l<size and array[l]>array[i]:
        largest=l
    if r<size and array[r]>array[largest]:
        largest=r
    if largest!=i:
        array[largest],array[i]=array[i],array[largest]
def heapSort(array):
    size=len(array)
    for i in range(size//2-1,-1,-1):
        heapify(array,size,i)
    for i in range(size-1,0,-1):
        array[i],array[0]=array[0],array[i]
        heapify(array,size,0)
array = [12, 11, 13, 5, 6, 7]
heapSort(array)
N = len(array)
print("Sorted array is")
print(array)