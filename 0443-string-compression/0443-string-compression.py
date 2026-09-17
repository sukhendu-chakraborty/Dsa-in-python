class Solution:
    def compress(self, chars: list[str]) -> int:
        i = 0
        j = 0
        while i<len(chars):
            char = chars[i]
            c= 0
            while i< len(chars) and chars[i]==char:
                i+=1
                c+=1
            chars[j]=char
            j+=1
            if c>1:
                for d in str(c):
                    chars[j]=d
                    j+=1
        return j


        