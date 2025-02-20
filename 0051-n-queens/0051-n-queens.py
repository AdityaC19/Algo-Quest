class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        grid = [['.'] * n for _ in range(n)]

        col = set()
        posDiag = set() # (r+c)
        negDiag = set() # (r-c)

        def backtracking(r):
            if r == n:
                copy = [''.join(row) for row in grid]
                return res.append(copy)

            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                grid[r][c] = 'Q'

                backtracking(r+1)

                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                grid[r][c] = '.'
        
        backtracking(0)
        return res







        



                
        