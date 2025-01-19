class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        max_w = 0
        l = 0
        max_freq = 0
        hashmap = {}

        for r in range(n):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            w = (r-l)+1
            max_freq =  max(max_freq, hashmap[s[r]])
            while w - max_freq > k:
                hashmap[s[l]] -= 1
                l += 1
                w = (r - l) + 1
        
            max_w = max(max_w, w)
        return max_w


            

        