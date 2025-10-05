class Solution:
    def romanToInt(self, s: str) -> int:
        hmap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        i = 0
        n = len(s)
        summ = 0

        while i < n:
            if i < n-1 and hmap[s[i]] < hmap[s[i+1]]:
                summ += hmap[s[i+1]] - hmap[s[i]]
                i += 2
            else:
                summ += hmap[s[i]]
                i += 1

        
        return summ

       