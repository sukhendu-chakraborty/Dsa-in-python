class Solution:
    def checkDivisibility(self, n: int) -> bool:
        p = 1
        s = 0
        temp = n
        while temp>0:
            s+=temp%10
            p*=temp%10
            temp//=10
        return n%(s+p)==0
        