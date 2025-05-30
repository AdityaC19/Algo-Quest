class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sol = []

        def isPalindrome(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def backtrack(i):
            if i == len(s):
                res.append(sol[:])
                return
            
            for x in range(i, len(s)):
                if isPalindrome(i, x):
                    sol.append(s[i:x+1])
                    backtrack(x+1)
                    sol.pop()
        
        backtrack(0)
        return res

        
        