class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class doublyLL:
    def __init__(self):
        self.head=None
    def insert_at_beg(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
    def print_ll(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp is not None:
                print(temp.data,'-->',end=" ")
                temp=temp.next
    def print_reverse(self):
        if self.head is None:
            print("ll is empty")
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            while temp is not None:
                print(temp.data,'-->',end="")
                temp=temp.prev
if __name__=='__main__':
    
    ll=doublyLL()
    ll.insert_at_beg(10)
    ll.insert_at_beg(11)
    ll.insert_at_beg(2)
    ll.print_ll()
    print("\n")
    ll.print_reverse()