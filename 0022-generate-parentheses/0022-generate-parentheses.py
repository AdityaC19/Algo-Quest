class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sol = []
        hmap = {'(':')'}
        stk = []

        # def validParenthesis():
        #     for i in range(n):
        #         if i in hmap:
        #             stk.append(i)
        #         elif stk and i == hmap[stk[-1]]:
        #             stk.pop()
        #         else:
        #             return False
            
        #     return not stk

        def backtrack(left, right, i):
            if len(i) == 2*n:
                res.append(i)
                return  
            
            if left < n: 
                #sol.append()
                backtrack(left + 1, right, i + '(')
            if right < left:
                #sol.append()
                backtrack(left, right + 1, i + ')')

        backtrack(0, 0, '')
        return res




            
                

            
        