class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        b = {}
        for i in range (n) :
            rem = target - nums[i]
            if rem in b:
                return [b[rem],i]
            else :
                b[nums[i]]=i


        