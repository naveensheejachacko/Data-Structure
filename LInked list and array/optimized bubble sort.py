def bubble(arr,n):
    for i in range(0,n-1):
        flag=0
        for j in range(0,n-1-i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                flag=1
        if flag==0:
            break
arr=[3,4,67,3,2,1,9]
n=len(arr)
print("array after sorting:",arr)
bubble(arr,n)
print("array after sorting:",arr)