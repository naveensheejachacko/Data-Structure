class Node:
    def _init_(self, data):
        self.next = None
        self.data = data
class Circle:
    def _init_(self):
        self.head = None
    def create(self):
        for i in range(1,101):
            newnode=Node(i)
            if self.head is None:
                self.head = newnode
            else:
                N = self.head
                while N.next is not None:
                    N = N.next
                N.next = newnode
            if i == 100:
                newnode.next = self.head
    def fire(self):
        N = self.head
        while N.next is not N:
            d = N.next
            N.next = d.next
            print("firing", d.data)
            del d
            N = N.next
        else:
            print("surviver is : ", N.data)
if __name__=="__main__":
    c = Circle()
    c.create()
    c.fire()