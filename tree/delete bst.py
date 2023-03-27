class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def delete_node(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = find_min_node(root.right)
        root.val = temp.val
        root.right = delete_node(root.right, temp.val)
    return root


def find_min_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def inorder(root):
    if root.left:
        inorder(root.left)
    print(root.val,end=" ")
    if root.right:
        inorder(root.right)

root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(8)
print("inorder traversal:")
inorder(root)
root = delete_node(root, 5)
print()
print("after deletion:")
inorder(root)
