class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
            }
        
        res = []
        sol = []
        n = len(digits)

        def backtracking(i):
            if not digits:
                return []
            
            if i == n:
                return res.append(''.join(sol[:]))
            
            for x in keyboard[digits[i]]:
                sol.append(x)
                backtracking(i+1)
                sol.pop()
                
        backtracking(0)
        return res


        