class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_c = {}
        for c in s:
            hash_c[c] = hash_c.get(c, 0) + 1

        for c in t:
            if not hash_c.get(c):
                return False
            hash_c[c] -= 1
        return True