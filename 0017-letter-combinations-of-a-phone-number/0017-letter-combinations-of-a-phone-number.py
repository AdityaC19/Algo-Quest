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

        def backtrack(i):
            if not digits:
                return 

            if len(sol) == n:
                res.append(''.join(sol[:]))
                return
            
            for char in keyboard[digits[i]]:
                sol.append(char)
                backtrack(i+1)
                sol.pop()
        
        backtrack(0)
        return res

