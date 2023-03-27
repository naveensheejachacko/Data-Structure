# # selection sort Ascending
# def selection_sort(arr,n):
#     for i in range(n):
#         for j in range(i+1,n):
#             if arr[i]>arr[j]:
#                 arr[i],arr[j]=arr[j],arr[i]
#     return arr
# arr=[24,2,5,67,4]
# print(arr)
# n=len(arr)
# s=selection_sort(arr,n)
# print(s)

# print("descending")
# #selection sort descending
# def descending(arr,n):
#     for i in range(n):
#         for j in range(i+1,n):
#             if arr[i]>arr[j]:
#                 arr[i],arr[j]=arr[j],arr[i]
#     return arr

# arr=[4,3,2,6,45,3,21]
# print(arr)
# n=len(arr)
# s=descending(arr,n)
# print(s)

def selection_sort (arr,n):
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if arr[min_index]>arr[j]:
                min_index=j    
        if min_index!=i:
            arr[min_index],arr[i]=arr[i],arr[min_index]

    
arr=[3,2,5,4,56,7,1,9]
print("array before sort:",arr)
n=len(arr)
selection_sort(arr,n)
print("array after sort:",arr)
