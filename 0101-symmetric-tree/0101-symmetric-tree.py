# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.resL = []
        self.resR = []
        
    def traverseL(self, root):
        if root is None:
            self.resL.append(-1)
            return 
            
        self.resL.append(root.val)
        self.traverseL(root.left)
        self.traverseL(root.right)
        
    def traverseR(self, root):
        if root is None:
            self.resR.append(-1)
            return 
            
        self.resR.append(root.val)
        self.traverseR(root.right) 
        self.traverseR(root.left)
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
            
        self.resL = []
        self.resR = []
        
        self.traverseL(root.left)
        self.traverseR(root.right)
        
        return self.resL == self.resR
