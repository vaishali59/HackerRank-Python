# Writing Tree Level wise
'''
       F
      / \
    D    J
   / \  / \
   B  E G  K
  / \    \
 A   C    I
          /
          H

Level   Node
1       F
2       D,J  
3       B,E,G,K
4       A,C,I
5       H

Order
F,D,J,B,E,G,K,A,C,I,H

'''
# Code:

class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

def LevelOrder(root):
    if root is None:
        return
    l=[]
    l.append(root)
    while len(l)>0:
        temp = l.pop(0)
        print(temp.data, end=" ")
        if temp.left:
            l.append(temp.left)
        if temp.right:
            l.append(temp.right)

root = Node("F") 
root.left = Node('D')

root.right = Node('J')

root.left.left = Node('B') 
root.left.right = Node('E')

root.right.left = Node('G') 
root.right.right = Node('K')

root.left.left.left =Node('A') 
root.left.left.right = Node('C')

root.right.left.right = Node('I') 
root.right.left.right.left = Node('H')  
print("Level order traversal is ") 
LevelOrder(root)
                
            
