class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Dll:
    def __init__(self):
        self.head=None
    def insert_beg(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node

    def insert_after(self,data,x):
        if self.head is None:
            print(" ll is empty")
        else:
            temp=self.head
            while temp is not None:
                if x==temp.data:
                    break
                temp=temp.next
            if temp is None:
                print("given node is not available")
            else:
                new_node=Node(data)
                new_node.next=temp.next
                new_node.prev=temp
                if temp.next is not None:
                    temp.next.prev=new_node
                temp.next=new_node





    def print(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp is not None:
                print(temp.data,'-->',end="")
                temp=temp.next
    
ll=Dll()
ll.insert_beg(10)
ll.insert_beg(20)
ll.print()
print('\n')
ll.insert_after(1,20)
ll.print()