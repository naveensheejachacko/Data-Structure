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


    def delete_by_value(self,x):
        if self.head is None:
            print("linked list is empty")
            return
        if x==self.head.data:
            self.head=self.head.next
            return
        temp=self.head
        while temp is not None:
            if x==temp.next.data:
                break
            temp=temp.next
        if temp.next is None:
            print("no nod is present")
        else:
            temp.next=temp.next.next

    def print(self):
        temp=self.head
        while temp:
            print(temp.data,'-->',end=" ")
            temp=temp.next
    
if __name__=='__main__':
    ll=LinkedList()
    ll.insert_at_beg(10)
    ll.insert_at_beg(13)
    ll.insert_at_beg(2)
    ll.print()
    print("\n")
    ll.delete_by_value(13)
    ll.print()