class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        res = []
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for n, f in count.items():
            freq[f].append(n)
        for i in reversed(freq):
            for n in i:
                res.append(n)
                if len(res) == k:
                    return res
        