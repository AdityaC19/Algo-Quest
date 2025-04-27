class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        store = set()
        longest = 0

        for r in range(len(s)):
            while s[r] in store:
                store.remove(s[l])
                l += 1
            store.add(s[r])
            w = (r-l) + 1
            longest = max(longest, w)
        
        return longest
        