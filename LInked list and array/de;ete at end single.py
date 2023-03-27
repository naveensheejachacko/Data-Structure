class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_beg(self,data):
        new_node=Node(data,self.head)
        self.head=new_node
    def delete_at_end(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
    def print(self):
        temp=self.head
        while temp:
            print(temp.data,'-->',end="")
            temp=temp.next
if __name__=='__main__':
    ll=LinkedList()
    ll.insert_at_beg(10)
    ll.insert_at_beg(14)
    ll.insert_at_beg(56)
    ll.print()
    print("\n")
    ll.delete_at_end()
    ll.print()