# tree insertion and inorder
class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def insert(node,key):
    if node==None:
        return Node(key)
    if node.data>key:
        node.left=insert(node.left,key)
    elif node.data<key:
        node.right=insert(node.right,key)
    return node

# inorder traversal
def inorder(node):
    if node.left:
        inorder(node.left)
    print(node.data,end=" ")
    if node.right:
        inorder(node.right)

# level order print
# def levelorder(node):
#     q=[]
#     q.append(node)
#     while q:
#         root=q.pop(0)
#         print(root.data)
#         if root.left is not None:
#             q.append(root.left)
#         if root.right is not None:
#             q.append(root.right)
        
# second largest
# def secondLargest(root):
#     c=[0]
#     secondLargestUtil(root,c)
# def secondLargestUtil(root,c):
#     if root is None or c[0]>=2:
#         return
#     secondLargestUtil(root.right,c)
#     c[0]+=1
#     if c[0]==2:
#         print("second largest is:",root.data)
#         return
#     secondLargestUtil(root.left,c)

# DELETEION
def min_value(node):
    current=node
    while current.left is not None:
        current=current.left
    return current
def delete(root,key):
    if root is None:
        return root
    if root.data>key:
        root.left=delete(root.left,key)
    elif root.data<key:
        root.right=delete(root.right,key)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
    temp=min_value(root.right)
    root.key=temp.key
    root.right=delete(root.right,temp.key)
root=None
root=insert(root,40)
insert(root,35)
insert(root,70)
insert(root,60)
insert(root,55)
inorder(root)
print()
delete(root,60)
# levelorder(root)
# secondLargest(root)