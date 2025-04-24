class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = defaultdict(list)

        for i in strs:
            sorted_str = ''.join(sorted(i))
            h[sorted_str].append(i)

        return list(h.values())

