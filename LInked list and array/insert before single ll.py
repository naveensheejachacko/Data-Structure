class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def appened(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node
    def insert_before(self,x,data):
        if self.head is None:
            print("linked list is empty")
        if self.head.data==x:
            new_node=Node(data)
            self.head.next=self.head
            self.head=new_node
        temp=self.head
        while temp.next:
            if temp.next.data==x:
                break
            temp=temp.next
        if temp.next is None:
            print("node not found")
        else:
            new_node=Node(data)
            new_node.next=temp.next
            temp.next=new_node
            
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,'-->',end='')
            temp=temp.next
        

if __name__=="__main__":
    ll=LinkedList()
    ll.appened(10)
    ll.appened(15)
    ll.appened(20)
    ll.display()
    print('\n')
    ll.insert_before(15,11)
    ll.display()