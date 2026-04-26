class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sorted_words = ''.join(sorted(s))
            res[sorted_words].append(s)
        return list(res.values())
       