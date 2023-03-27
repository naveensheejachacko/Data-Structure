class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_beg(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
        else:
                new_node.next=self.head
                self.head=new_node
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,'-->',end='')
                temp=temp.next
if __name__=='__main__':
    ll=LinkedList()
    ll.insert_at_beg(10)
    ll.insert_at_beg(24)
    ll.insert_at_beg(30)
    ll.display()