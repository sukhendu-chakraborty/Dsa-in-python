class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        l = 0
        r = 1
        while r < len(intervals):
            if intervals[l][1] >= intervals[r][0]:
                intervals[l][1] = max(intervals[r][1],intervals[l][1])
                del intervals[r]
            else:
                l=r
                r+=1
        return intervals



        

        