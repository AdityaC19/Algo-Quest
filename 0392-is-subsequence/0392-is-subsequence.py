class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:       
        
        if len(s) == 0: return True
        if len(s) > len(t): return False
        
        curr = 0
        for i in range(len(t)):
            if s[curr] == t[i]:
                if curr == len(s)-1:
                    return True
                curr += 1
    
        return False