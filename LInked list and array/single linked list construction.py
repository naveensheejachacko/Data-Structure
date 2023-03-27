class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class LinkedList:
    def __init__(self):
        self.head=None
    def appened(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp
    def display(self):
        if self.head is None:
            print("linked list is empty")
        temp=self.head
        while temp:
            print(temp.data,'-->',end='')
            temp=temp.next

if __name__=='__main__':
    ll=LinkedList()
    ll.appened(10)
    ll.appened(14)
    ll.appened(32)
    ll.display()