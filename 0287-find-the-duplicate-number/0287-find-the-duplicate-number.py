class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        s  = nums[0]
        f = nums[0]
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if f == s:
                break
            
        s = nums[0]
        while s != f:
            s = nums[s]
            f = nums[f]
        return s
