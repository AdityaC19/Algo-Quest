class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = float('inf')

        for str in strs:
            if len(str) < min_len:
                min_len = len(str)
        
        ans = []
        strs = sorted(strs)
        for i in range(min_len):
            if strs[0][i] == strs[-1][i]:
                ans.append(strs[0][i])
            else: 
                break
        
        return ''.join(ans)



        

        