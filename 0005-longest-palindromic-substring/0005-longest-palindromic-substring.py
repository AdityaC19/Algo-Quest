class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        l = 0
        r = 0
        maxLen = 0
        ans = []

        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if (r-l+1) > maxLen:
                    ans = s[l:r+1]
                    maxLen = r-l+1
                l-=1
                r+=1
            
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if (r-l+1) > maxLen:
                    ans = s[l:r+1]
                    maxLen = r-l+1
                l-=1
                r+=1
        
        return ans

        