def heapify(array,n,i):
    large=i
    l=2*i+1
    r=2*i+2
    if l<n and array[l]>array[i]:
        large=l
    if r<n and array[r]>array[large]:
        large=r
    if large!=i:
        array[i],array[large]=array[large],array[i]
def insert(array):
    size=len(array)
    for i in range((size//2)-1,-1,-1):
        heapify(array,size,i)
def delete(array,num):
    for i in range(0,len(array)):
        if num==array[i]:
            break
    array[i],array[len(array)-1]=array[len(array)-1],array[i]
    array.remove(num)
    for i in range((len(array)//2)-1,-1,-1):
        heapify(array,len(array),i)


array=[3,4,5,2,9]
insert(array)
print("max heap:",str(array))
delete(array,5)
print("max heap:",str(array))