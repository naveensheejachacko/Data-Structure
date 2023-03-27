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

    def get_length(self):
        count=0
        temp=self.head
        while temp:
            count+=1
            temp=temp.next
            return count
    def insert_at_pos(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception("invlid linked List")

        count=0
        temp=self.head
        while temp:
            if count==index-1:
                new_node=Node(data,temp.next)
                temp.next=new_node
                break
            temp=temp.next
            count+=1

    def print(self):

        temp=self.head
        llstr=''
        while temp:
            llstr+=str(temp.data)+'-->'
            temp=temp.next
            print(llstr)

if __name__=='__main__':
    ll=LinkedList()
    ll.insert_at_beg(39)
    ll.insert_at_pos(1,100)
    ll.insert_at_beg(45)

    ll.insert_at_pos(1,10)
    ll.insert_at_pos(1,15)
    ll.print()
