class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = " ".join(s.split())
        a = r.split(" ")
        b = a[-1]
        return len(b)
        