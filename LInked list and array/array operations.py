# # # find element
# # def findElement(arr,n,key):
# #     for i in range(n):
# #         if arr[i]==key:
# #             return i
# #     return -1


# # if __name__=="__main__":
# #     arr=[23,54,5,3,2,36]
# #     n=len(arr)
# #     key=36
# #     index=findElement(arr,n,key)
# #     if index !=-1:
# #         print("Element found at:"+str(index+1))
# #         print("\n")
# #     else:
# #         print("element not found")



# # #insert value 

# # def insert(arr,key):
# #     arr.append(key)


# # if __name__=="__main__":
# #     arr=[4,2,43,65,76,8]
# #     key=45
# #     print("array before inserting:"+str(arr))
# #     index=insert(arr,key)
# #     print("elements after insertion:"+str(arr))
# # # insert at postion
# # arr=[2,5,4,7,8,10]
# # arr.insert(2,54)
# # print(arr)
# # print("\n")

# # #remove value 
# # arr=[2,5,4,7,8,10]
# # print("array before remove:"+str(arr))
# # arr.remove(4)
# # print("array after removal:"+str(arr))



# # #lucky or not



# #palindrome r no

# # class Solution:
# #     def isPalindrome(self,x):
# #         rev=0
# #         num=x
# #         if x<0:
# #             return False
# #         while x!=0:
# #             rev= (rev*10) + x%10
# #             x = x//10

            
# #         if rev==num:
# #             print("true")
# #             return True
# #         else:
# #             print("false")
# #             return False
# # if __name__=="__main__":
# #     sol=Solution()    
# #     sol.isPalindrome(123)


# # array insert

# # class Array_insert:
# #     def insert_pos(self,pos,data):
# #         for i in range(n-1,pos-1 ,-1):
# #             arr[i]=arr[i-1]
# #         arr[pos-1]=data
        


# # if __name__=="__main__":
# #     arr=[12,34,21,45,32]
# #     print(arr)
# #     n=len(arr)
# #     array_insert=Array_insert()
# #     array_insert.insert_pos(2,90)
# #     print(arr)


# # class Solution:
# #     def removeDuplicates(self, nums: list[int]) -> int:
# #         if len(nums)== 0:
# #             return 0
# #         count=0
# #         for right in range(0,len(nums)-1):
# #             if nums[right]!=nums[count]:
# #                 count+=1
# #                 nums[count]=nums[right]
            
                
# #         return nums
# # if __name__=='__main__':
    
# #     nums=[1,4,4,5,6,7,8]
# #     print(nums)
# #     s=Solution()
# #     s.removeDuplicates(nums)
# #     print(nums)

# #find index
# # class Solution:
# #     def searchInsert(self, nums: List[int], target: int) -> int:
# #         if target in nums:
# #             return nums.index(target)
# #         else:
# #             nums.append(target)
# #             return sorted(nums).index(target)



# # Python program to implement
# # the above approach


# # 35. Search Insert Position
# # Function to find insert position of K


# # Time Complexity: O(log N)
# # Auxiliary Space: O(1)
# # def find_index(arr, n, B):

# # 	# Lower and upper bounds
# # 	start = 0
# # 	end = n - 1

# # 	# Traverse the search space
# # 	while start<= end:

# # 		mid =(start + end)//2

# # 		if arr[mid] == K:
# # 			return mid

# # 		elif arr[mid] < K:
# # 			start = mid + 1
# # 		else:
# # 			end = mid-1

# # 	# Return the insert position
# # 	return end + 1

# # # Driver Code
# # arr = [1, 3, 5, 6,8,9]
# # n = len(arr)
# # K = 7
# # print(find_index(arr, n, K))




# # 21. merge two soted linked list


# """ Python program to merge two
# sorted linked lists """


# # Linked List Node
# class Node:
# 	def __init__(self, data):
# 		self.data = data
# 		self.next = None


# # Create & Handle List operations
# class LinkedList:
# 	def __init__(self):
# 		self.head = None

# 	# Method to display the list
# 	def printList(self):
# 		temp = self.head
# 		while temp:
# 			print(temp.data,'-->', end=" ")
# 			temp = temp.next

# 	# Method to add element to list  end
# 	def addToList(self, newData):
# 		newNode = Node(newData)
# 		if self.head is None:
# 			self.head = newNode
# 			return

# 		temp = self.head
# 		while temp.next:
# 			temp = temp.next

# 		temp.next = newNode


# # Function to merge the lists
# # Takes two lists which are sorted
# # joins them to get a single sorted list
# def mergeLists(headA, headB):

# 	# A dummy node to store the result
# 	dummyNode = Node(0)

# 	# Tail stores the last node
# 	tail = dummyNode
# 	while True:

# 		# If any of the list gets completely empty
# 		# directly join all the elements of the other list
# 		if headA is None:
# 			tail.next = headB
# 			break
# 		if headB is None:
# 			tail.next = headA
# 			break

# 		# Compare the data of the lists and whichever is smaller is
# 		# appended to the last of the merged list and the head is changed
# 		if headA.data <= headB.data:
# 			tail.next = headA
# 			headA = headA.next
# 		else:
# 			tail.next = headB
# 			headB = headB.next

# 		# Advance the tail
# 		tail = tail.next

# 	# Returns the head of the merged list
# 	return dummyNode.next


# # Create 2 lists
# listA = LinkedList()
# listB = LinkedList()

# # Add elements to the list in sorted order
# listA.addToList(5)
# listA.addToList(10)
# listA.addToList(15)

# listB.addToList(2)
# listB.addToList(3)
# listB.addToList(20)

# # Call the merge function
# listA.head = mergeLists(listA.head, listB.head)

# # Display merged list
# print("Merged Linked List is:")
# listA.printList()


# # 66. Plus One
# class Solution:
# 	def plusOne(self):
# 		one=1
# 		i=0
# 		while one:
# 			if i<len(digits):
# 				if digits[i]==9:
# 					digits[i]=0
# 				else:
# 					digits[i]+=1
# 			else:
# 				digits.append(1)
# 				one=0
# 			i+=1



# digits=[1,2,3,4]
# print(digits)
# s=Solution()
# s.plusOne()
# print(digits)




class Solution:
    def twoSum(self,arr,target):

        for i in range(0,len(arr)-1):
            for j in range(i+1,len(arr)):
                if (arr[i]+arr[j] == target):
                    return i,j

if __name__=="__main__":
	s=Solution()
	arr=[1,2,3,8,6,7]
	target=9
	a=s.twoSum(arr,target)
	print(a)

