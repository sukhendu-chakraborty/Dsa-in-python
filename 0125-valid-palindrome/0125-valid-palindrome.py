class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = "".join(char for char in s if char.isalnum())
        a= cleaned_text.lower()
        return a == a[::-1]     