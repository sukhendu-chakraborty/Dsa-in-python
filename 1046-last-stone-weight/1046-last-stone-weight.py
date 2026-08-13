import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        heapq.heapify(h)
        for i in stones:
            heapq.heappush(h,-i)
        while len(h)>1:
            a = -(heapq.heappop(h))
            b = -(heapq.heappop(h))
            c = a-b
            if c>0:
                heapq.heappush(h,-c)
        if len(h) == 0:
            return 0
        else:
            return -h[0]