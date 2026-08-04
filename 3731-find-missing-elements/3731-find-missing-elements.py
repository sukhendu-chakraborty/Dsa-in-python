class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        if not nums:                      
            return []
        min_n = min(nums)
        max_n = max(nums)
        n = []
        for i in range(min_n, max_n+1):
            n.append(i)
        main_set= set(nums)
        set_n = set(n)
        return sorted(set_n - main_set)




        