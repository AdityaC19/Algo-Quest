class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict(int)

        if len(s) != len(t): return False

        for i in s:
            d[i] += 1
        
        for i in t:
            if i in d and d[i] == 1:
                del d[i]
            elif i in d:
                d[i] -= 1
            else:
                return False
        
        return True if len(d) == 0 else False
        

