class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sol = []

        def isPalindrome(start, end):
            return s[start:end+1] == s[start:end+1][::-1]

        def backtracking(i):
            if i == len(s):
                return res.append(sol[:])
            
            #backtracking(i+1)

            for end in range(i, len(s)):
                if isPalindrome(i, end):
                    sol.append(s[i:end+1])
                    backtracking(end + 1)
                    sol.pop()
                
        backtracking(0)
        return res

        