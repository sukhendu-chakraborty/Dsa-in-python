class Solution:
    def reverse(self, num: int) -> int:
        if num > (2 ** 31)-1:
            return 0
        if num < 0:
            a =  -int(str(abs(num))[::-1])
            if -a > (2 ** 31)-1:
                return 0
            else:
                return a
    
        a = int(str(num)[::-1])
        if a > (2 ** 31)-1:
            return 0
        else:
            return a

        