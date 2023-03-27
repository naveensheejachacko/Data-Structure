class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Dll:
    def __init__(self):
        self.head=None
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp
    def print(self):
        if self.head is None:
            print("linked list is not valid")
        else:
            temp=self.head
            while temp is not None:
                print(temp.data,'-->',end="")
                temp=temp.next

ll=Dll()
ll.insert_at_end(100)
ll.insert_at_end(20)
ll.print()