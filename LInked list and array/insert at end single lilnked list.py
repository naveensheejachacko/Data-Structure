class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_end(self,new_data):
        new_node=Node(new_data) 
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=new_node
    def print(self):
        temp=self.head
        llstr=''
        while (temp):
            llstr+=str(temp.data)+'-->'
            temp=temp.next
            print(llstr)
if __name__=='__main__':
    ll=LinkedList()
    ll.insert_at_end(45)
    ll.insert_at_end(56)
    ll.print()


