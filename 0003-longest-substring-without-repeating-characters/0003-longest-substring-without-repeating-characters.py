class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        seen = set()
        max_len = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            w = (r-l) + 1
            max_len = max(max_len, w)
        
        return max_len
        