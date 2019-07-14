#Top-View Binary Tree
'''
         1
       /   \
      2     3
     / \   / \
    4   5  6  7

'''
import collections
class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

def TopView(self):
    if root is None:
        return

    l=[] # for level order traversal
    hd_node={} 
    m={}

    l.append(root)
    hd_node[root]=0
    m[0]=[root.data]

    while len(l)>0:
        temp=l.pop(0)
        if temp.left:
            l.append(temp.left)
            hd_node[temp.left]=hd_node[temp]-1
            hd=hd_node[temp.left]
            if m.get(hd) is None:
                m[hd]=[]
            m[hd].append(temp.left.data)

        if temp.right:
            l.append(temp.right)
            hd_node[temp.right]=hd_node[temp]+1
            hd=hd_node[temp.right]
            if m.get(hd) is None:
                m[hd]=[]
            m[hd].append(temp.right.data)

    sorted_m=collections.OrderedDict(sorted(m.items()))

    for i in sorted_m.values():
        print(i[0],end=" ")

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

    

    
