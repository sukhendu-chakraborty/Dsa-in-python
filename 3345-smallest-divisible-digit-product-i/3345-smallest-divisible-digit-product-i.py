class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            p  = 1
            for digit in str(n):
                p*= int(digit)
            if p%t == 0:
                return n
                break
            else:
                n+=1
        