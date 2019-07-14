#Insertion
'''
    4
   / \
  2   7
 / \
1   3

'''
class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)

def inOrder(root):
    if root == None:
        return
    inOrder(root.left)
    print (root.info, end=" ")
    inOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insertion(self,root,node):
            if node.info<root.info:
                if not root.left:
                    root.left =node
                else:
                    self.insertion(root.left,node)
            if node.info>root.info:
                if not root.right:
                    root.right=node
                else:
                    self.insertion(root.right,node)
                    
    def insert(self,val):
        newNode=Node(val)
        if self.root is None:
            self.root=newNode
        else:
            self.insertion(self.root,newNode)
                
tree = BinarySearchTree()
#t = int(input())
#arr = list(map(int, input().split()))
#for i in range(t):
#    tree.insert(arr[i])
tree.insert(4)
tree.insert(2)
tree.insert(7)
tree.insert(1)
tree.insert(3)
inOrder(tree.root)
