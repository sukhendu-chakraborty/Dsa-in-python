class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        longest = ""
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]
        for i in range(len(s)):
            odd_p = expand(i, i)
            if len(odd_p) > len(longest):
                longest = odd_p
            even_p = expand(i,i+1)
            if len(even_p) > len(longest):
                longest = even_p
        return longest
            


        