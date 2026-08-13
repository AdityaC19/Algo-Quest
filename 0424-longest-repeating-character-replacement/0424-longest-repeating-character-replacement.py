class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0 
        r = 0
        hmap = defaultdict(int)
        maxFreq = 0
        ans = 0

        for r in range(n):
            hmap[s[r]] += 1
            maxFreq = max(maxFreq, hmap[s[r]])

            while (r-l+1) - maxFreq > k:
                hmap[s[l]] -= 1
                l += 1
            
            ans = max(ans, r-l+1)
        
        return ans


