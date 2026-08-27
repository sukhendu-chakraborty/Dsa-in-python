class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        l = 0
        for r in range (1,len(intervals)):
            if intervals[l][1] >= intervals[r][0]:
                intervals[l][1] = max(intervals[r][1],intervals[l][1])
            else:
                l+=1
                intervals[l] = intervals[r]
        return intervals[:l + 1]



        

        