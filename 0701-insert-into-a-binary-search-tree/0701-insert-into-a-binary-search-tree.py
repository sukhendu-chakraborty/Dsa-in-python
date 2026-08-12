# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:    
        curr = root
        nn = TreeNode()
        nn.val = val
        if root is None:
            root = nn
            return root

        while True:
            if curr.val > val:
                if curr.left != None:
                    curr = curr.left
                else:
                    curr.left = nn
                    break
            else:
                if curr.right != None:
                    curr = curr.right
                else:
                    curr.right = nn
                    break
        return root

        