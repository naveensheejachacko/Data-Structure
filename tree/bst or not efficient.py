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
previous=None
def isBST(root):
	global previous
	previous=None
	return isBST_inorder(root)
def isBST_inorder(root):
	global previous
	if root is None:
		return True
	if isBST_inorder(root.lchild) is False:
		return False
	if previous is not None and previous.data>root.data:
		return False
	previous=root
	return isBST_inorder(root.rchild)



root=BST(10)
list1=[2,43,1,56,4,24,8,7,12]
for i in list1:
    root.insert(i)
print("preorder:")
root.preorder()
print()
if(isBST(root)):
    print("Binary Tree is BST")
else:
    print("Binary Tree is not Bst")