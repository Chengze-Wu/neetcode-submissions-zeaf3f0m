class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = set()

        left = 0
        maxLength = 0

        for right in range(len(s)):
            if s[right] not in count:
                count.add(s[right])
            else:
                
                while s[left] != s[right]:
                    count.remove(s[left])
                    left += 1
                left += 1
            maxLength = max(right - left + 1, maxLength)
        return maxLength
        