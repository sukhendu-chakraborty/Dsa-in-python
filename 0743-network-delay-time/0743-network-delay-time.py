from heapq import heappush,heappop
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjlist = [[] for i in range(n)]
        for time in times:
            x= time[0]-1
            y= time[1]-1
            w = time[2]
            adjlist[x].append([y,w])
        heap = []
        dist = [float("inf")]*n
        k-=1
        dist[k]=0
        heappush(heap,(dist[k],k))
        while len(heap)>0:
            d,u = heappop(heap)
            for v,w in adjlist[u]:
                if d + w < dist[v]:
                    dist[v]=d+w
                    heappush(heap,(dist[v],v))
        ans = max(dist)
        if ans == float("inf"):
            return -1
        else:
            return ans

        