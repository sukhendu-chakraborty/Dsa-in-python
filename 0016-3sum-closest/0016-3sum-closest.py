import math
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        snums = sorted(nums)
        i=0
        max_diff = math.inf
        diff = 0
        closest_sum=0
        while i < (len(snums)-2):
            if i > 0 and snums[i] == snums[i - 1]:
                i += 1
                continue
            l = i +1
            r = len(snums)-1
            while l<r:
                ts= snums[l]+snums[r]+snums[i]
                if (ts==target):
                    return target
                    break
                elif (ts > target):
                    diff = abs(ts-target)
                    if (max_diff>diff):
                        max_diff=diff
                        closest_sum=ts
                    r-=1
                else :
                    diff = abs(ts-target)
                    if (max_diff>diff):
                        max_diff=diff
                        closest_sum=ts
                    l+=1
            i+=1
        return closest_sum
        