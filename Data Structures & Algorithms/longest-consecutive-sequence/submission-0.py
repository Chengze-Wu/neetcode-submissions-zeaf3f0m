class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequence = set(nums)
        length = 0
        for n in sequence:
            if n - 1 not in sequence:
                i = 1
                currentLength = 1
                while n + i in sequence:
                    currentLength += 1
                    i += 1
                length = max(length, currentLength)
        return length
        