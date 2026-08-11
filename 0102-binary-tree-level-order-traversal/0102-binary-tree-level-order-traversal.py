# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Queue:
    def __init__(self):
        self.q =[]
        self.front=-1
    def push(self,x):
        if self.front==-1:
            self.q.append(x)
            self.front+=1
        else:
            self.q.append(x)
    def pop(self):
        if self.front == -1 or self.front >= len(self.q): 
            self.front = -1  # Reset if empty
            return -1 
        val = self.q[self.front] 
        self.front += 1 
        return val
    def get_front(self):
        if self.front == -1 or self.front >= len(self.q): 
            return None 
        return self.q[self.front]
    def size(self):
        if self.front == -1:
            return 0
        return len(self.q) - self.front
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = Queue()
        ans = []
        if root is None:
            return ans
        q.push(root)
        ans.append([root.val])
        while q.size()>0:
            l = q.size()
            lvl = []
            for i in range(l):
                f  = q.pop()
                if f.left != None:
                    q.push(f.left)
                    lvl.append(f.left.val)
                if f.right != None:
                    q.push(f.right)
                    lvl.append(f.right.val)

            if len(lvl)>0:
                ans.append(lvl)

        return ans

        