class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        sl = list(s)
        result = 0
        prev = 0
        curr = 1
        for r in range (1,len(sl)):
            if sl[r]==sl[r-1]:
                curr += 1
                if prev >= curr:
                    result+=1
            else:
                prev = curr
                curr = 1
                if prev >= curr:
                    result+=1
        return result
                

        