class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        short = min(len(word1), len(word2))

        ans = []

        for i in range(short):
            ans.append(word1[i])
            ans.append(word2[i])
        
        ans.append(word1[short:])
        ans.append(word2[short:])

        return ''.join(ans)
        
        