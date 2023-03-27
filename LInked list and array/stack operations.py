class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
    def push(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
    def pop(self):
        if self.head is None:
            print("stack is empty")
        else:
            temp=self.head
            self.head=self.head.next
            temp.next=None
    def peek(self):
        if self.head is None:
            print("stack is empty")
        else:
            print("the top element is:",self.head.data)
    def display(self):
        if self.head is None:
            print("stack is empty")
        else:
            print("the stack is:")
            temp=self.head
            while temp:
                print(temp.data,'-->',end="")
                temp=temp.next                

if __name__=='__main__':
    obj=Stack()
    obj.display()
    obj.push(120)
    obj.push(110)
    obj.push(100)
    obj.display()
    print("\n")
    obj.pop()
    obj.display()
    print("\n")
    obj.peek()