class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        l = 1
        r = x
        ans = 1
        while l<=r:
            mid = (l+r)//2
            sqrtx = mid*mid
            if sqrtx>x:
                r = mid-1
            else:
                ans = mid
                l = mid+1
        return ans

        