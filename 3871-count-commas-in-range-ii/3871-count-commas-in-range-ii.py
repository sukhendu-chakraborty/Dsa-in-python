class Solution:
    def countCommas(self, n: int) -> int:
        if n <= 999:
            return 0
        total = 0
        th = 1000
        while (n>=th):
            total += (n - th + 1)
            th *= 1000
        return total


        