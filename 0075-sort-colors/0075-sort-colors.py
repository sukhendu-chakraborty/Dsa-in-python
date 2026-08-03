class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        frq= [0,0,0]
        for i in nums:
            frq[i]+=1
        ind = 0
        for i in range(3):
            while frq[i]>0:
                nums[ind]=i
                ind+=1
                frq[i]-=1
        
        