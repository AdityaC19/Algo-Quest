class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []

        n = min(len(word1), len(word2))

        i = 0
        for i in range(n):
            ans.append(word1[i])
            ans.append(word2[i])
        
        ans.append(word1[i+1:])
        ans.append(word2[i+1:])

        return "".join(ans)




        
        