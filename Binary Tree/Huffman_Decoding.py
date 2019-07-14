# Tree Huffman Coding
'''
    null
    / \
null   A
/ \     
B  C

'''

class Node():
    def __init__(self,data):
        self.data=data
        self.left=self.right=None
        
s="1001011"
def decodeHuff(root , s):
   #Enter Your Code Here
    temp=root
    string=[]
    for i in s:
        c=int(i)
        if c==1:
            temp=temp.right
        elif c==0:
            temp=temp.left
        if temp.right==None and temp.left==None:
            string.append(temp.data)
            temp=root
    b=''.join(string)
    print b

root=Node("Null")
root.left=Node("Null")
root.right=Node("A")
root.left.left=Node("B")
root.left.right=Node("C")
decodeHuff(root,s)
