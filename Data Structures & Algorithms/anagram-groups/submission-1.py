class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # result = []
        # str_hash = {}
        # for s in strs:
        #     key = "".join(sorted(s))
        #     if key not in str_hash:
        #         str_hash[key] = [s]
        #     else:
        #         str_hash[key].append(s)
        # for value in str_hash.values():
        #     result.append(value)
        
        # return result

        # res = defaultdict(list)
        # for s in strs:
        #     key = "".join(sorted(s))
        #     res[key].append(s)
        
        # return list(res.values())
        # return res
        
        res = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
            