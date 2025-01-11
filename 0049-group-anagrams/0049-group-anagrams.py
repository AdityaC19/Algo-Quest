class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        ans = []
        for i in strs:
            sorted_str = ''.join(sorted(i))
            if sorted_str in h:
                ans[h[sorted_str]].append(i)
            else:
                h[sorted_str] = len(ans)
                ans.append([i])

        return ans
