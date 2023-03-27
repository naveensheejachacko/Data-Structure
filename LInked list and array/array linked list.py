
# class Solution:
#     def twoSum(self,arr,target):
#         list=[]
#         var=0
#         for i in range(0,len(arr)-1):
#                 var==target-arr[i]
                
#                 if var in i:
#                     list=[]
#         return list

# if __name__=="__main__":
# 	s=Solution()
# 	arr=[1,2,3,8,6,5]


# 	target=9
# 	a=s.twoSum(arr,target)
# 	print(a)

#reverse array
# class Sample:
#     def reverse(self,arr,n):
#         start=0
#         end=n-1
#         while start<end:
#             arr[start],arr[end]=arr[end],arr[start]
#             start+=1
#             end-=1
# if __name__=="__main__":
#     arr=[1,2,3,4,5]
#     print(arr)
#     s=Sample()
#     n=len(arr)
#     s.reverse(arr,n)
#     print(arr)

#minikmum and maximum in an array

# class Sample:
#     def Solution(self,arr,n):
#         for i in range(0,n):
#             for j in range(i+1,n):
#                 if arr[i]>arr[j]:
#                     arr[i],arr[j]=arr[j],arr[i]
#         return arr
# if __name__=='__main__':
#     arr=[7,5,7,4,3,21,45,67,6,7,9,2]
#     print(arr)
#     n=len(arr)
#     s=Sample()
#     s.Solution(arr,n)
#     print(arr[0],arr[n-1])


#odd and interger in seperate array
# class Sample:
#     def solution(self,arr,n):
#         o=[]
#         e=[]
#         for i in range (0,n,1):
#             if arr[i]%2==0:
#                 e.append(arr[i])
#             else:
#                 o.append(arr[i])
#         print(o,e) 
        



# if __name__=="__main__":
#     arr=[1,2,3,4,5,6,7,8,9]
#     n=len(arr)
#     s=Sample()
#     s.solution(arr,n)
    

# python 3 program to implement
# binary search in sorted array


# def binarySearch(arr, low, high, key):

# 	mid = (low + high)/2

# 	if (key == arr[int(mid)]):
# 		return mid

# 	if (key > arr[int(mid)]):
# 		return binarySearch(arr,(mid + 1), high, key)

# 	if (key < arr[int(mid)]):
# 		return binarySearch(arr, low, (mid-1), key)

# 	return 0


# # Driver code
# if __name__ == "__main__":
# 	# Let us search 3 in below array
# 	arr = [5, 6, 7, 8, 9, 10]
# 	n = len(arr)
# 	key = 10

# 	# Function call
# 	print("Index:", int(binarySearch(arr, 0, n-1, key)))

# Python program to reverse a linked list
# Time Complexity : O(n)
# Space Complexity : O(n) as 'next'
#variable is getting created in each loop.

# Node class

#reverse linked list
class Node:
	def __init__(self,data,next):
		self.data=data
		self.next=next
class LinkedList:
	def __init__(self):
		self.head=None
	def push(self,new_data):
		new_node=Node(new_data,self.head)
		new_node.next=self.head
		self.head=new_node
	def reverse(self):
		prev=None
		temp=None
		while self.head:
			temp=self.head
			self.head=temp.next
			temp.next=prev
			prev=temp
		self.head=temp
		return temp
	def printList(self):
		if self.head is None:
			print("linked lst is empty")
			return
		temp=self.head
		while temp:
			print(temp.data,"-->",end="")
			temp=temp.next

# Driver program to test above functions
if __name__=='__main__':
	llist = LinkedList()
	llist.push(20)
	llist.push(4)
	llist.push(15)
	llist.push(85)

	print ("Given Linked List")
	llist.printList()
	llist.reverse()
	print ("\nReversed Linked List")
	llist.printList()

