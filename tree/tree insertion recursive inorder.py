class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root==key:
            return root
        elif root.val<key:
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val,end=" ")
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val,end=" ")

if __name__=="__main__":
    r=Node(20)
    r=insert(r,19)
    r=insert(r,8)
    r = insert(r, 3)
    r = insert(r, 15)
    r = insert(r, 34)
    r = insert(r, 17)
    r = insert(r, 22)
    r = insert(r, 73)
    r = insert(r, 65)
    print("\n inorder:")
    inorder(r)
    print("\n preorder:")
    preorder(r)
    print("\n postorder:")
    postorder(r)