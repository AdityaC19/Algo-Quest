class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = defaultdict(int)
        maxFreq = 0
        l = 0
        max_len = 0

        for r in range(len(s)):
            hmap[s[r]] += 1
            maxFreq = max(maxFreq, hmap[s[r]])
            while (r-l+1) - maxFreq > k:
                hmap[s[l]] -= 1
                l += 1
            w = (r-l) + 1
            max_len = max(max_len, w)
        
        return max_len


        