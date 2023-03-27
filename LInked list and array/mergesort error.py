def merge_sort(arr,low,high):
    if low<high:
        mid=low+high//2
        merge_sort(arr,low,mid)
        merge_sort(arr,mid+1,high)

        #merging
        i=low
        j=mid+1
        value=0
        while i<=mid and j<=high:
            if arr[i]<=arr[j]:
                i+=1
            else:
                value=arr[j]
                index=j
                while index !=1:
                    arr[index]=arr[index-1]
                    index=index-1
            arr[i]=value
            i+=1
            j+=1
            mid+=1
arr=[12,3,4,21,1,24,2,9]
high=len(arr)
low=0
print(arr)
sol=merge_sort(arr,low,high)
print(sol)


