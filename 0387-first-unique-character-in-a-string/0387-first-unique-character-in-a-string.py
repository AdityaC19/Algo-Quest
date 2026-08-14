class Solution:
    def firstUniqChar(self, s: str) -> int:
        hmap = {}

        for i in range(len(s)):
            if s[i] not in hmap:
                hmap[s[i]] = 1
            else:
                hmap[s[i]] += 1
        
        for i in range(len(s)):
            if hmap[s[i]] ==1:
                return i
        
        return -1



        