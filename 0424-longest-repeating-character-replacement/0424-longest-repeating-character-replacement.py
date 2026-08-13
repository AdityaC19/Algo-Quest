class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        hmap = defaultdict(int) # {A:0, B:0}
        maxFreq = 0
        ans = 0

        l = 0

        for r in range(n):
            hmap[s[r]] += 1
            maxFreq = max(maxFreq, hmap[s[r]])

            #k = window len - maxFreq
            while (r-l+1) - maxFreq > k:    #invalid cond
                hmap[s[l]] -= 1
                l += 1

            ans = max(ans, (r-l+1))

        return ans



        