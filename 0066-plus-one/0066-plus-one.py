class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = int("".join(map(str, digits)))
        num  = result+1
        return [int(digit) for digit in str(num)]
        