class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = Counter(s)

        if len(s) != len(t): return False

        for i in t:
            if i in smap and smap[i] == 1:
                del smap[i]
            elif i in smap:
                smap[i] -= 1
            else:
                return False
        
        return True if len(smap) == 0 else False

                      
            
            

        
        

        

        