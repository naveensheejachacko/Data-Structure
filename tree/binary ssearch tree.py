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
            self.lchild.insert(key)
        else:
            self.lchild=BST(key)
        if self.data<key:
            self.rchild.insert(key)
        else:
            self.lchild=BST(key)
    def preorder(self):
        print(self.data,'-->',end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
root=BST(10)
array=[3,5,4,12,65,80]
for i in array:
    root.insert(i)
root.preorder()