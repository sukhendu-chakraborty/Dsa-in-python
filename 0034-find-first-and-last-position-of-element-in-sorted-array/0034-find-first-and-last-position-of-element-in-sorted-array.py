class Solution:
    def lb(self, nums, target):
        n = len(nums)
        l = 0
        r = n-1
        ans = -1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]>=target:
                ans = mid
                r = mid-1
            else:
                l = mid +1
        return ans
    def hb(self, nums, target):
        n = len(nums)
        l = 0
        r = n-1
        ans = -1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]>target:
                ans = mid
                r = mid-1
            else:
                l = mid +1
        return ans-1 if ans != -1 else n - 1
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a = self.lb(nums, target)
        b = self.hb(nums, target)
        if a == -1 or nums[a] != target:
            return [-1, -1]
        return [a,b]
        

