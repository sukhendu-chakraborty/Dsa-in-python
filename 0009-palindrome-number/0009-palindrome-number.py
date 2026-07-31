class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x1 = [int(i) for i in str(x)]
        rev_x1 = list(reversed(x1))
        if x1 == rev_x1:
            return True
        else:
            return False