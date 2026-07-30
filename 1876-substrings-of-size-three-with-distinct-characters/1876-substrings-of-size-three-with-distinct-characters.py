class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range (len(s)-2):
            if s[i]==s[i+1] or s[i+1]==s[i+2] or s[i]==s[i+2]:
                i += 1
            else:
                count += 1
        return count

