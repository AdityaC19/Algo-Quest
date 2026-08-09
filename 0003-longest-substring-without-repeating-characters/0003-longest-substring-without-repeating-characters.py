class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        ans = 0
        l, r = 0, 0

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l +=1
            seen.add(s[r])
            ans = max(r-l+1, ans)
            #print(seen, ans)
            r += 1

        return ans



        