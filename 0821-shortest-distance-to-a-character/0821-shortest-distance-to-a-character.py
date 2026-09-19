class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)
        res = [0]*n
        p = float('inf')
        for i in range(n):
            if s[i]==c:
                p = i
            res[i] = abs(i-p)
        p = float('inf')
        for i in range(n-1,-1,-1):
            if s[i]==c:
                p = i
            res[i] = min(res[i],abs(i-p))

        return res