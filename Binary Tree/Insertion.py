#Insertion
'''
    4
   / \
  2   7
 / \
1   3

'''

class Node():
    def __init__(self,info):
        self.info=info
        self.left=self.right=None
        
def insert(root,node):
    if root is None:
        root=node
    else:
        if root.info<node.info:
            if root.right is None:
                root.right=node
            else:
                insert(root.right,node)
        else:
            if root.left is None:
                root.left=node
            else:
                insert(root.left,node)
                
def inorder(root):
    if root:
        inorder(root.left)
        print()

