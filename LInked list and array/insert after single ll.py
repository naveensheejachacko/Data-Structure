class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tale=None
    def appened(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tale=new_node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next  
            temp.next=new_node
            self.tale=new_node
    def insert_after(self,x,data):
        temp=self.head
        while temp:
            if temp.data==x:
                break
            temp=temp.next
        if temp is None:
            print("invalid value")
        else:
            new_node=Node(data)
            new_node.next=temp.next
            temp.next=new_node
    def display(self):
        tale=self.tale
        temp=self.head
        while temp:
            print(temp.data,'-->',end='')
            temp=temp.next
        


if __name__=='__main__':
    ll=LinkedList()
    ll.appened(10)
    ll.appened(20)
    ll.display()
    print('\n')
    ll.insert_after(10,15)
    ll.display()