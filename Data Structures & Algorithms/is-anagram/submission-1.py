class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_c = {}
        for c in s:
            if c in hash_c:
                hash_c[c] += 1
            else:
                hash_c[c] = 1

        for c in t:
            if c in hash_c and hash_c[c] > 0:
                hash_c[c] -= 1
            else:
                return False
        return True