class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        sol = []

        def backtrack(open, close):
            if len(sol) == 2*n:
                ans.append(''.join(sol[:]))
                return
            
            if open < n:
                sol.append('(')
                backtrack(open+1, close)
                sol.pop()
            
            if close < open:
                sol.append(')')
                backtrack(open, close+1)
                sol.pop()
        
        backtrack(0, 0)
        return ans
        


        