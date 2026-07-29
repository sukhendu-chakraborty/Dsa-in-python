class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numsa = set(nums1)
        numsb = set(nums2)
        return list(numsa & numsb)
        