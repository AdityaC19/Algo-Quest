class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        count  = [0] * 26
        maxLen = 0

        for r in range(n):
            count[ord(s[r]) - 65] += 1

            while (r-l+1) - max(count) > k:
                count[ord(s[l]) - 65] -= 1
                l += 1
            
            maxLen = max(maxLen, r-l+1)

        return maxLen

        