class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_beg(self,data):
        new_node=Node(data,self.head)
        self.head=new_node


    def delete_at_beg(self):
        if self.head is None:
            print("not a valid linked list")
        else:
            self.head=self.head.next
    def print(self):

        temp=self.head
        llstr=''
        while temp:
            print(temp.data,'-->',end='')
            temp=temp.next
          
    
if __name__=='__main__':
    ll=LinkedList()
    ll.insert_at_beg(39)

    ll.insert_at_beg(45)
    ll.delete_at_beg()

    ll.print()