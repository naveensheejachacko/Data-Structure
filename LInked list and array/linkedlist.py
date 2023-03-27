# # class Node:
# #     def __init__(self,data=None,next=None):
# #         self.data=data
# #         self.next=next
# # class LinkedList:
# #     def __init__(self):
# #         self.head=None


# # #insert at beginnning
# #     def insert_at_beg(self,data):
# #         new_node=Node(data,self.head)



# #     def print(self):
# #         if self.head is None:
# #             print('linked list empty')
# #             return
# #         temp=self.head
# #         llstr=''
# #         while temp:
# #             llstr+=str(temp.data)+'-->'
# #             temp=temp.next
# #             print(llstr)

# # if __name__=='__main__':
# #     ll=LinkedList()
# #     ll.insert_at_beg(5)
# #     ll.insert_at_beg(10)
# #     ll.print()






# # # insert at specific  position

# # # class Node:
# # #     def __init__(self,data=None,next=None):
# # #         self.data=data
# # #         self.next=next

# # # class LinkedList:
# # #     def __init__(self):
# # #         self.head=None
# # #     def insert_at_beg(self,data):
# # #         node=Node(data,self.head)
# # #         self.head=node

# # # # insert at beginnning
# # #     def insert_at_beg(self,data):
# # #         new_node=Node(data,self.head)
# # #         self.head=new_node


    

# # #     def print(self):
# # #         if self.head is None:
# # #             print('linked list empty')
# # #             return
# # #         temp=self.head
# # #         llstr=''
# # #         while temp:
# # #             llstr+=str(temp.data)+'-->'
# # #             temp=temp.next
# # #             print(llstr)

# # # if __name__=="__main__":
# # #     ll=LinkedList()
# # #     ll.insert_at_beg(15)
# # #     ll.insert_at_beg(11)

# # #     ll.print()    

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class LinkedList:
#     def __init__(self):
#         self.head=None
#     def insert_at_beg(self,data):
#         new_node=Node(data)
#         new_node.next=self.head
#         self.head=new_node

#     def insert_at_end(self,data):
#         new_node=Node(data)
#         if self.head is None:
#             self.head=new_node
           
           
#         else:
#             temp=self.head
#             while temp.next is not None:
#                 temp=temp.next
#             temp.next=new_node

# #insert after
#     def add_after(self,data,x):
#         temp=self.head
#         while temp is not None:
#             if temp.data==x:
#                 break
#             temp=temp.next
#         if temp is None:
#             print( "node not found")
#         else:
#             new_node=Node(data)
#             new_node.next=temp.next
#             temp.next=new_node


#     def add_before(self,data,x):
#         if self.head is None:
#             print("empty linked list")
#         if x==self.head.data:
#             new_node=Node(data)
#             new_node.next=self.head
#             self.head=new_node
#             return
#         temp=self.head
#         while temp.next is not None:
#             if temp.next.data==x:
#                 break
#             temp=temp.next
#         if temp.next is None:
#             print("no node found")
#         else:
#             new_node=Node(data)
#             new_node.next=temp.next
#             temp.next=new_node

#     def delete_begin(self):
#         if self.head is None:
#             print("ll is empty")
#         else:
#             self.head=self.head.next
            
#     def delete_end(self):
#         if self.head is None:
#             print("linked list is empty")
#         temp=self.head
#         while temp.next.next is not None:
#             temp=temp.next
#         temp.next=None


#     def delete_by_value(self,x):
#         if self.head is None:
#             print("LL is empty")

#         if self.head.data==x:
#             self.head=self.head.next
#             return

#         temp=self.head
#         while temp.next is not None:
#             if temp.next.data==x:
#                 break
#             temp=temp.next
#         if temp is None:
#             print("node not found")
#         else:
#             temp.next=temp.next.next 


#     def print(self):
#         if self.head is None:
#             print("linked lst is empty")
#             return
#         temp=self.head
#         while temp is not None:
#             print(temp.data,'-->',end="")
#             temp=temp.next
# ll=LinkedList()
# ll.insert_at_beg(10)
# ll.insert_at_beg(11)
# ll.insert_at_beg(34)
# ll.print()
# print("\n")
# # ll.add_before(2,11)
# ll.print()
# print("\n")
# # ll.delete_by_value(2)
# # ll.delete_begin()
# ll.print()
# print("\n")
# # ll.delete_end()

# ll.print()
