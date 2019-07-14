#Top-View Binary Tree
'''
         1
       /   \
      2     3
     / \   / \
    4   5  6  7

'''
class Node:
    def __init__(self,info):
        self.info=info
        self.left=self.right=None
        self.level=0

def TopView(root):
    if root is None:
        return
    q=[]
    level=0
    root.level=level
    m={}

    q.append(root)

    while len(q):
        temp=q.pop(0)
        level=temp.level

        if level not in m:
            m[level]=temp.info

        if temp.left:
            temp.left.level=temp.level-1
            q.append(temp.left)

        if temp.right:
            temp.right.level=temp.level+1
            q.append(temp.right)

    for i in sorted(m):
        print(m[i],end=" ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)

#root.left.left = Node(4)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.left.right.right.right = Node(6)

#root.right.left = Node(6)
#root.right.right = Node(7)
print("Following are nodes in top view of Binary Tree")
TopView(root)
