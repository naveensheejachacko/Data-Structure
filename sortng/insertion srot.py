def insertion_sort(arr,n):
    for i in range(1,n):
        temp=arr[i]
        j=i-1
        while (j>=0 and arr[j]>temp):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp
arr=[10,9,8,5,6,7,3]
n=len(arr)
print("array before insertion sort:",arr)
insertion_sort(arr,n)
print("array after insertion sort:",arr)