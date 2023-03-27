class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=self.rear=None
    def isEmpty(self):
        return self.front==None
    def Enqueue(self,data):
        temp=Node(data)
        if self.rear is None:
            self.front=self.rear=temp
            return
        self.rear.next=temp
        self.rear=temp

    def Dequeue(self):
        if self.isEmpty():
            return
        temp=self.front
        self.front=temp.next
        temp.next=None
        if self.front==None:
            self.rear=None
if __name__=='__main__':
    q=Queue()
    q.Enqueue(10)
    q.Enqueue(20)
    q.Enqueue(30)
    print("\n queue front:",q.front.data)
    print("\n queue rear:",q.rear.data)
    q.Dequeue()
    print("\n queue front:",q.front.data)
