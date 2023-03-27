class Node:
    def __init__(self,value):
        self.value=value
        self.children=[]
    def add_children(self,node):
        self.children.append(node)
    def delete_child(self,value):
        for i,child in enumerate(self.children):
            if child.value==value:
                del self.children[i]
                return
            else:
                child.delete_child(value)
    def display(self,level=0):
        print("  " * level+self.value)
        for child in self.children:
            child.display(level+1)

root=Node("A")
b=Node("B")
c=Node("C")
d=Node("D")
e=Node("E")
root.add_children(b)
root.add_children(c)
b.add_children(d)
b.add_children(e)
root.display()
print("tree after deletion")
root.delete_child("C")
root.display()







                