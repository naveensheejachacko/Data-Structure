arr=[1,2,3,4,5]
arr.append(6)
arr.insert(2,4)
arr.remove(5)
print(arr)

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node


