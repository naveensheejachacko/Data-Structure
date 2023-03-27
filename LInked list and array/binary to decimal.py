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
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node
    def displayLL(self):
        temp=self.head
        while temp:
            print(temp.data,'-->',end='')
            temp=temp.next
    def binary_to_decimal(self):
        answer=0
        temp=self.head
        while temp:
            answer=2*answer+temp.data
            temp=temp.next
        return answer
ll=LinkedList()
ll.appened(1)
ll.appened(1)
ll.appened(0)
ll.appened(1)
ll.appened(0)
ll.displayLL()
print("\n")
val=ll.binary_to_decimal()
print(val)




    # def binary_to_decimal(self):
    #     decimal = 0
    #     current_node = self.head
    #     position = 0
    #     while current_node is not None:
    #         decimal += decimal*2+current_node.data
    #         current_node = current_node.next
    #         position += 1
    #     return decimal
    
