class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = [0] * 26
        for c in s1:
            count1[ord(c) - ord('a')] += 1

        for i in range(len(s2) - len(s1) + 1):
            count2 = [0] * 26
            s = s2[i:i+len(s1)]
            for c in s:
                count2[ord(c) - ord('a')] += 1
            if count2 == count1:
                return True
        return False