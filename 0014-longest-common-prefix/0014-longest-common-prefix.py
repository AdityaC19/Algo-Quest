class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs[0])
        strs.sort()

        for s in strs:
            n = min(len(s), n)

        ans = []
        for i in range(n):
            if strs[0][i] != strs[-1][i]:
                break
            else:
                ans.append(strs[0][i])
        
        return "".join(ans)



        