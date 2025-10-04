class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        shorter = min(len(word1), len(word2))
        ans = []

        for i in range(shorter):
            ans.append(word1[i])
            ans.append(word2[i])

        ans.append(word1[shorter:])
        ans.append(word2[shorter:])
    
        return "".join(ans)
