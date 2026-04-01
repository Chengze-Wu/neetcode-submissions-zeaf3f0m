class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        unique = {}
        maxLength = 0
        if len(s) == 0:
            return 0
        for right in range(len(s)):
            if s[right] not in unique: 
                unique[s[right]] = right
                
            else:
                left = max(unique[s[right]] + 1, left)
                unique[s[right]] = right    
            maxLength = max(right - left + 1, maxLength)
        return maxLength
        