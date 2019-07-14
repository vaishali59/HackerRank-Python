# Vertical Order Traversal
'''
        1
       /  \
      2     3
     / \  /  \
    4   5 6    7
           \  /  \
            8 10  9
                \
                11
                  \
                   12
'''
#Code:

import collections
class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

def VerticalOrderTraversal(root):
    if root is None:
        return
    l=[]
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
        for j in i:
            print(j,end=" ")
        print()

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
root.right.left.right =Node(8) 
root.right.right.left = Node(10) 
root.right.right.right = Node(9) 
root.right.right.left.right = Node(11) 
root.right.right.left.right.right = Node(12) 
print("Vertical order traversal is ") 
VerticalOrderTraversal(root) 
        
        
