class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        res = []
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for n, f in count.items():
            freq[f].append(n)
        for l in reversed(freq):
            if l and len(res) != k:
                res += l
        return res
        