class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        def countPalindrome(s, l, r):
            res = 0
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res

        for i in range(n):
            res += countPalindrome(s, i, i)
            res += countPalindrome(s, i, i+1)

        return res





        