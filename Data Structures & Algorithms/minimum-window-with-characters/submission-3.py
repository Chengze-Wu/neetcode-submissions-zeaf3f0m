class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        resLen = float("infinity")
        res = [-1, -1]
        count_t, count_s = {}, {}
        l = 0
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
        need, have = len(count_t), 0
        for r in range(len(s)):
            c = s[r]
            count_s[c] = count_s.get(c, 0) + 1
            if c in count_t and count_s[c] == count_t[c]:
                have += 1
            while need == have:
                if (r- l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                count_s[s[l]] -= 1
                # Update have
                if s[l] in count_t and count_t[s[l]] > count_s[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""