class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        l = 0
        chrr = {}
        c = 0
        for r in range(len(s)):
            chrr[s[r]] = chrr.get(s[r], 0) + 1
            while chrr[s[r]] > 2:
                chrr[s[l]] -= 1
                l += 1
            c = max(c, r - l + 1)   
        return c

        