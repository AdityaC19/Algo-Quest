class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = len(strs[0])
        ans = []

        for i in strs:
            if len(i) < min_len:
                min_len = len(i)
        
        strs = sorted(strs)
        for i in range(min_len):
            if strs[0][i] == strs[-1][i]:
                ans.append(strs[0][i])
            else:
                break
        
        return ''.join(ans)

        