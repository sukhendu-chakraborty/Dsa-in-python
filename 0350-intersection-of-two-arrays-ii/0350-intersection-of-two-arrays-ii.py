class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = {}
        for n in nums1:
            c[n] = c.get(n,0)+1
        r = []
        for n in nums2:
            if c.get(n,0) > 0:
                r.append(n)
                c[n]-=1
        return r

        