class Node:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None
def identical(a,b):
    if a is None and b is None:
        return True
    if a is not None and b is not None:
        return ((a.data==b.data) and identical(a.lchild,b.lchild) and identical(a.rchild,b.rchild))
    return False

root1=Node(1)
root2=Node(1)
root1.lchild=Node(2)
root2.lchild=Node(2)
root1.rchild=Node(3)
root2.rchild=Node(3)
if __name__=="__main__":
    if identical(root1,root2):
        print("identical")
    else:
        print("not binary tree")




# Time Complexity: O(min(N, M)), Where N and M are the sizes of the trees
# Auxiliary Space: O(log min(N, M)), due to auxiliary stack space used by recursion calls