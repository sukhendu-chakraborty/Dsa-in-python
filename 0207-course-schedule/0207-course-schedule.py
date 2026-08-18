class Queue:
    def __init__(self):
        self.q = []
        self.front = -1
    def push(self, item):
        if self.front == -1:
            self.front = 0
        self.q.append(item)
    def pop(self):
        if not self.is_empty():
            return self.q.pop(0)
        else:
            return None
    def get_front(self):
        if not self.is_empty():
            return self.q[self.front]
        else:
            return None
    def size(self):
        return len(self.q)
    def is_empty(self):
        return len(self.q) == 0
class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        q = Queue()
        ans = []
        indeg = [0]*n
        adjlist =[[]for i in range (n)]
        for a,b in prerequisites:
            indeg[a]+=1
            adjlist[b].append(a)
        for j in range(n):
            if indeg[j]==0:
                ans.append(j)
                q.push(j)
        while q.size()>0:
            front = q.pop()
            for x in adjlist[front]:
                indeg[x]-=1
                if indeg[x]==0:
                    ans.append(x)
                    q.push(x)
        if len(ans)==n:
            return True
        return False

                

        