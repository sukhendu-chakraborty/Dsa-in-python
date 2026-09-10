# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.r = 0
        def dfs(node: TreeNode) -> None:
            if not node:
                return 0, 0
            left_c, left_s = dfs(node.left)
            right_c, right_s =dfs(node.right)
            curr_c = left_c + right_c + 1
            curr_s = left_s + right_s + node.val
            if curr_s // curr_c == node.val:
                self.r += 1
            return curr_c, curr_s
        dfs(root)
        return self.r
        
        