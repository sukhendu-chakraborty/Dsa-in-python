class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        t = max(arr)
        l = 0
        r = len(arr)-1
        while l<=r:
            mid = l + (r-l)//2
            if arr[mid]==t:
                return mid
            elif arr[mid]<arr[mid+1]:
                l = mid+1
            else:
                r = mid-1

        