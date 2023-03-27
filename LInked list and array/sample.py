
# class Node:
#     def __init__(self,data=None,next=None):
#         self.data=data
#         self.next=next
# class LinkedList:
#     def __init__(self):
#         self.head=None
#     def insert_beg(self,data):
#         node = Node(data,self.head)
#         self.head=node
#     def print(self):
#         if self.head is None:
#             print('linked list is empty')
#             return
#         itr =self.head
#         llstr= ''
#         while itr:
#             llstr+= str(itr.data) +'-->'
#             itr=itr.next
#         print(llstr)
#     def insert_at_end(self,data):
#         if self.head is None:
#             self.head=Node(data,None)
#             return
#         itr=self.head
#         while itr.next:
#             itr=itr.next
#         itr.next=Node(data,None)

# if __name__ =='__main__':
#     ll=LinkedList()
#     ll.insert_beg(10)
#     ll.insert_beg(55)
#     ll.insert_at_end(50)
#     ll.insert_at_end(43)
#     ll.print()


# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    # def get_length(self):
    #     count=0
    #     itr=self.head
    #     while itr:
    #         count+=1
    #         itr=itr.next
    #     return count

    def insertAfter(self,prev_node,new_data):
        if prev_node is None:
            print("must be a linked list")
            return
        new_node=Node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node

    # def insert_at(self,index,data):
    #     if index<0 or index>self.get_length():
    #         raise Exception("invalid linked list")
    #     if index==0:
    #         self.push(data)
    #         return
    #     count=0
    #     itr=self.head
    #     while itr:
    #         if count==index-1:
    #             node=Node(data,itr.next)
    #             itr.next=node
    #             break
    #         itr=itr.next
    #         count=+1


    def append(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node



    # def print(self):
    #     if self.head is None:
    #         print('linked list is empty')
    #         return
    #     itr =self.head
    #     llstr= ''
    #     while itr:
    #         llstr+= str(itr.data) +'-->'
    #         itr=itr.next
    #     print(llstr)
    def print(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ",)
            temp=temp.next
        print(end='\n')


if __name__ =='__main__':
    ll=LinkedList()
    ll.push(9)
    ll.push(155)
    ll.push(34)
    ll.print()

    ll.insertAfter(ll.head.next,99)
    ll.print()
    # ll.append(20)
    # ll.print()
    # ll.insert_at(1,10)
    # ll.print()
