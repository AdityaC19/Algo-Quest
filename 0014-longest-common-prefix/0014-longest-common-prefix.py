class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        n = len(strs[0])

        for s in strs:
            n = min(n, len(s))
        
        ans = []
        for i in range(n):
            if strs[0][i] != strs[-1][i]:
                break
            else:
                ans.append(strs[0][i])
        
        return ''.join(ans)

        