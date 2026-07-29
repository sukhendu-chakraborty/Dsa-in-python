class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        f= {}
        for ch in s:
            if ch not in f:
                f[ch]=1
            else:
                f[ch]+=1
        for i in t:
            if i not in f:
                return False
            else:
                f[i]-=1
        for i  in f.values():
            if i!=0:
                return False

        return True



        