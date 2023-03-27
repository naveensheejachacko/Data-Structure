class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def remove_duplicates(self):
        temp=self.head
        if temp is None:
            return
        while temp.next is not None:
            if temp.data==temp.next.data:
                new=temp.next.next
                temp.next=new
            else:
                temp=temp.next
        return self.head
    def print(self):
        temp=self.head
        while temp:
            print(temp.data,'-->',end="")
            temp=temp.next

ll=LinkedList()
ll.push(20)
ll.push(21)
ll.push(21)
ll.push(21)
ll.push(23)
ll.push(24)
ll.push(24)
ll.push(26)
ll.print()
print("\n")
ll.remove_duplicates()
ll.print()