class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        seen = set()
        i = 0
        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0
        
        for j in range(len(s)):
            while s[j] in seen:
                seen.remove(s[i])
                i+=1
            seen.add(s[j])
            count = max(count, j-i+1)




        return count
        