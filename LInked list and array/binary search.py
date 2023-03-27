# binary search possible in a sorted array
class Solution:
    def binarySearch(self,arr,key):
        start=0
        end=len(arr)-1
        mid=0
        while start<=end:
            mid=(start+end)//2
            if arr[mid]<key:
                start=mid+1
            elif arr[mid]>key:
                end=mid-1
            else:
                print(mid)
                break
        return -1


if __name__=='__main__':
    arr=[1,2,3,4,5,6,7]
    print(arr)
    key=2
    s=Solution()
    s.binarySearch(arr,key)
 
