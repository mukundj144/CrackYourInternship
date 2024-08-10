#Function to count number of nodes in BST that lie in the given range.
class Solution:
    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left) 
        self.temp.append(node)  
        self.inorder(node.right) 
        
    def getCount(self,root,low,high):
        ##Your code here
        count=0
        self.temp=[]
        self.inorder(root)
        
        for node in self.temp:
            if low <= node.data <= high:
                count += 1
        
        return count 
