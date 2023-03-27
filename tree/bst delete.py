class BST:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None
    def insert(self,key):
        if self.data is None:
            self.data=key
        if self.data==key:
            return
        if self.data>key:
            if self.lchild:
                self.lchild.insert(key)
            else:
                self.lchild=BST(key)
        if self.data<key:
            if self.rchild:
                self.rchild.insert(key)
            else:
                self.rchild=BST(key)
    def preorder(self):
        print(self.data,end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
def min_value(node):
    current=node
    while current.lchild is not None:
        current=current.lchild
    return current
def delete(root,key):
    if root is None: 
        return root
    if root.data>key:
        root.lchild=delete(root.lchild,key)
    elif root.data<key:
        root.rchild=delete(root.rchild,key)
    else:
        if root.lchild is None:
            temp=root.rchild
            root=None
            return temp
        elif root.rchild is None:
            temp=root.lchild
            root=None
            return temp
    # finding smallest value in the rchild subtree if two nodes are present
        temp=min_value(root.rchild)
        root.data=temp.data
        root.rchild=delete(root.rchild,temp.data)
    return root
root=BST(10)
list1=[2,43,1,56,4,24,8,7,12]
for i in list1:
    root.insert(i)
print("preorder:")
root.preorder()
root=delete(root,2)
print()
print("value after deletion:")
root.preorder()
