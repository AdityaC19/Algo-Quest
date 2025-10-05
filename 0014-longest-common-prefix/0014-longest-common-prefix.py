class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = len(strs[0])
        ans = []
        for str in strs:
            min_len = min(min_len, len(str))
                
        strs = sorted(strs)
        for i in range(min_len):
            if strs[0][i] == strs[-1][i]:
                ans.append(strs[0][i])
            else:
                break
        
        return ''.join(ans)


        