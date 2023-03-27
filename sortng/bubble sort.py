# bubble sort ascending
print("bubble sort ascending")
def bubble_sort(arr,n):
    for i in range(n-1):
        for j in range(0,n-1-i):
            if arr[i]<arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr

arr=[2,5,12,4,2,54,8]
print("array before sorting",arr)
print("\n")
n=len(arr)
s=bubble_sort(arr,n)
print("array after sorting",s)
print("\n")




print("bubble sort descending")
print("\n")
#bubble sort descending
def bubble_desc(arr,n):
    for i in range(n):
        for j in range(0,n):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr

arr=[12,2,1,2,45,3,2,6,5,8]
print("array before sorting",arr)
print("\n")
n=len(arr)
s=bubble_desc(arr,n)
print("array after sorting",s)
