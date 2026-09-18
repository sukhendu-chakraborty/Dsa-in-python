class Solution:
    def reverseVowels(self, s: str) -> str:
        def is_vowel(char):
            vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
            return char in vowels
        s_list = list(s)

        l = 0
        r = len(s)-1
        while l < r:
            if not is_vowel(s_list[l]):
                l += 1
            elif not is_vowel(s_list[r]):
                r -= 1
            else:
                s_list[l], s_list[r] = s_list[r], s_list[l]
                l += 1
                r -= 1
                
        return "".join(s_list)
            

        