class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(i, j, k):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
            
            if k == len(word)-1:
                return True
            
            char = board[i][j]
            board[i][j] = '#'

            if dfs(i+1, j, k+1) or dfs(i, j+1, k+1) or dfs(i-1, j, k+1) or dfs(i, j-1, k+1):
                return True
            
            board[i][j] = char
        
        for x in range(m):
            for y in range(n):
                if dfs(x, y, 0):
                    return True
        
        return False
            


            

        