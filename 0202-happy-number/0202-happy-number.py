class Solution:
    def isHappy(self, n: int) -> bool:
        def next(k):
            s = 0
            while k >0:
                b=k % 10
                s+=b**2
                k = k//10
            return s
        f = next(n)
        s = n
        while (f!=1 and f!=s):
            s = next(s)
            f = next(next(f))
        return f==1

        