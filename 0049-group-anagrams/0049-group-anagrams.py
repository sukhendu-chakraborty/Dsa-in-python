class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_str = {}
        for i in strs:
            key = "".join(sorted(i))
            if key in sort_str:
                sort_str[key].append(i)
            else :
                sort_str[key] = [i]
        return list(sort_str.values())



            

        