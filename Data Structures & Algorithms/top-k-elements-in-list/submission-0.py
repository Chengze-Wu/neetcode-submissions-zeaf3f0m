class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        sorted_counts = sorted(counts.items(),key=lambda x: x[1], reverse = True)
        res = []

        for i in range(k):
            res.append(sorted_counts[i][0])
        return res