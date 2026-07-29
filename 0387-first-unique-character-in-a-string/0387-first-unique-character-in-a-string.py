class Solution:
    def firstUniqChar(self, s: str) -> int:
        f = {}
        for ch in s:
            if ch not in f:
                f[ch]=1
            else:
                f[ch]+=1
        for a in range(len(s)):
            if f [s[a]]==1:
                return a

        return -1
