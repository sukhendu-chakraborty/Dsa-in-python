# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = True
    def height(self,root):
        if root is None:
            return 0
        lH = self.height(root.left)
        rH = self.height(root.right)
        if abs(lH-rH) >1:
            self.ans = False
        return max(lH, rH) + 1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.height(root)
        return self.ans