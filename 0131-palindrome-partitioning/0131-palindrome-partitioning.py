class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sol = []

        def isPalindrome(start, end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

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

        