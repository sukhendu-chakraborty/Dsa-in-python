class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        sortd = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        return list(sortd.keys())[:k]