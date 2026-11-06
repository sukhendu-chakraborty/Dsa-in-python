class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = []
        c1, c2 = 0, 0
        can1, can2 = None, None
        for num in nums:
            if num==can1:
                c1+=1
            elif num == can2:
                c2+=1
            elif c1 == 0:
                can1 = num
                c1=1
            elif c2 == 0:
                can2 = num
                c2=1
            else:
                c1-=1
                c2-=1
        ac1 = sum(1 for num in nums if num==can1)
        ac2 = sum(1 for num in nums if num==can2)
        if ac1 > n//3:
            ans.append(can1)
        if can1!=can2 and ac2 > n//3:
            ans.append(can2)
        return ans




        