class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for current_index, num in enumerate(nums):
            if num in seen and current_index - seen[num] <= k:
                return True
            seen[num] = current_index
            
        return False
