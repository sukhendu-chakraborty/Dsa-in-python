class Solution:
    def hour (self, piles, mid):
        ans = 0
        for i in piles:
            ans+= (i+mid-1)//mid
        return ans

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r =max(piles)
        k = r
        if h == len(piles):
            return r
        else:
            while l<=r:
                mid = (l+r)//2
                if self.hour(piles,mid)>h:
                    l = mid+1
                else:
                    k = mid
                    r = mid-1
        return k




        