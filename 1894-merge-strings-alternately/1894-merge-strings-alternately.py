class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        shorter = min(len(word1), len(word2))
        l = []
        for i in range(shorter):
            l.append(word1[i])
            l.append(word2[i])
        
        l.append(word1[shorter:])
        l.append(word2[shorter:])
    
        return ''.join(l)
        
        
        