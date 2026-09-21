class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        l = 0
        r = k
        c = sum(nums[l:r])
        m = c
        while r<len(nums):
            c+= nums[r] - nums[l]
            if c>m:
                m = c
            l+=1
            r+=1
        return m/k


        