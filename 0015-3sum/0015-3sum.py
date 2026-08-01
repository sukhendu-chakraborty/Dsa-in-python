class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        snums=sorted(nums)
        result = []
        i = 0
        while i < (len(snums)-2):
            if i > 0 and snums[i] == snums[i - 1]:
                i += 1
                continue
            l = i +1
            r = len(snums)-1
            while l<r:
                if (snums[i]+snums[l]+snums[r] == 0):
                    result.append([snums[i],snums[l],snums[r]])
                    l+=1
                    r-=1
                    while l<r and (snums[l]==snums[l-1]):
                        l+=1
                    while l<r and (snums[r]==snums[r+1]):
                        r-=1
                elif (snums[i]+snums[l]+snums[r] > 0):
                    r-=1
                else :
                    l+=1
            i+=1
        return result
            



        

