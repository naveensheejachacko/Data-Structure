class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_beg(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    
    def print(self):
        temp=self.head
        llstr=''
        while (temp):
            llstr+=str(temp.data)+'-->'
            temp=temp.next
            print(llstr)

        