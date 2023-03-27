class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:


    

    def __init__(self):
        self.head=None
    def append(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
    def decimal_to_bin(self,decimal):
        binaryList=LinkedList()
        while decimal>0:
            remainder=decimal%2
            binaryList.append(remainder)
            decimal=decimal//2
        return binaryList
    def reverse(self):
        print('hello')
        prev=None
        temp=None
        while self.head:
            print('while')
            temp=self.head
            temp.next=prev
            prev=temp
            print(self.head.data,'-->',end='')
        self.head=prev
    def printll(self):
        temp=self.head
        print(temp)
        while temp:
            print(temp.data,'-->',end='')
            temp=temp.next
        
if __name__=='__main__':
    ll=LinkedList()
    ll.decimal_to_bin(10)
    ll.printll()
# def decimal_to_binary(num):
#     binary = ""
#     while num > 0:
#         binary = str(num % 2) + binary
#         num = num // 2
#     return binary

# print(decimal_to_binary(25))