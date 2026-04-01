class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        left = 0
        count = defaultdict(int)
        maxFreq = 0
        for right in range(len(s)):
            count[s[right]] += 1
            maxFreq = max(maxFreq, count[s[right]])
            if right - left + 1 - maxFreq > k:
                count[s[left]] -= 1
                left += 1
            maxLength = max(right - left + 1, maxLength)
        return maxLength


        