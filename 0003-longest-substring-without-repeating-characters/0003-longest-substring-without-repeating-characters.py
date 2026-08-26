class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        n = len(s)

        l , r = 0, 0
        maxLen = 0

        for r in range(n):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            maxLen = max(maxLen, (r-l+1))
            
        
        return maxLen





        
        