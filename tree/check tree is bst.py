class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def maxValue(node):
    if node is None:
        return 0
    leftMax=maxValue(node.left)
    rightMax=maxValue(node.right)
    value=0
    if leftMax>rightMax:
        value=leftMax
    else:
        valule=rightMax
    if value<node.data:
        value=node.data
    return value
def minValue(node):
    if node is None:
        return 100000000
    leftMax=minValue(node.left)
    rightMax=minValue(node.right)
    value=0
    if leftMax<rightMax:
        value=leftMax
    else:
        value=rightMax
    if value>node.data:
        value=node.data
    return value
def isBST(node):
    if node is None:
        return True
    if (node.left is not None and maxValue(node.left)>node.data):
        return False
    if (node.right is not None and minValue(node.right)<node.data):
        return False
    if (isBST(node.left) is False and isBST(node.right) is False):
        return False
    return True
if __name__=="__main__":
    root=Node(4)
    root.left=Node(2)
    root.right=Node(5)
    root.left.left=Node(1)
    root.left.right=Node(3)
    if isBST(root) is True:
        print("it is BST")
    else:
        print("it is not a BST")