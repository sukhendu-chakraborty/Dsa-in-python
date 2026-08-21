class Solution:
    def maxArea(self, h: List[int]) -> int:
        max_cap = 0
        l = 0
        r = len(h)-1
        while l<r:
            curr_cap = min(h[l],h[r])*(r-l)
            if curr_cap>max_cap:
                max_cap = curr_cap
            if h[l]<h[r]:
                l+=1
            else:
                r-=1
        return max_cap


        