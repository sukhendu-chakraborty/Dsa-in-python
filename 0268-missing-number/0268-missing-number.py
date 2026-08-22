class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        a = set(list(range(n + 1)))
        b = set(nums)
        c = list(a-b)
        return c[0]