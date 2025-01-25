class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = []
        index_complete = []
        m, n = len(board), len(board[0])

        def backtrack(i,j, k):
            if k == len(word):
                return True
            if i >= m or j >= n or i < 0 or j < 0 or board[i][j] != word[k]:
                return False
            
            char = board[i][j]
            board[i][j] = '#'

            if backtrack(i, j+1, k+1) or backtrack(i+1, j, k+1) or backtrack(i-1, j, k+1) or backtrack(i, j -1, k+1):
                return True  

            board[i][j] = char
            return False      

        for a in range(m):
            for b in range(n):
                if backtrack(a,b,0):
                    return True

        return False
        
     

            
                        


        