class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_board = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
            }

        sol = []
        res = []
        n = len(digits)
        
        if n == 0: return []

        def backtrack(i):
            if len(sol) == n:
                res.append(''.join(sol[:]))
                return

            for x in phone_board[digits[i]]:
                sol.append(x)
                backtrack(i+1)
                sol.pop()
        
        backtrack(0)
        return res

