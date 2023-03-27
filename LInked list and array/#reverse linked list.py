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
		self.head=prev
		# self.head=temp
		# return temp
	def printList(self):
		if self.head is None:
			print("linked lst is empty")
			return
		temp=self.head
		while temp:
			print(temp.data,"-->",end="")
			temp=temp.next


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