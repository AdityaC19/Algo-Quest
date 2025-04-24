class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = Counter(s)
        tmap = Counter(t)

        if smap == tmap:
            return True
        return False

                      
            
            

        
        

        

        