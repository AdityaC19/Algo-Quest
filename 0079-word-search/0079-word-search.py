class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(i, j, k):
            if k == len(word):
                return True

            # out of bounds conditions or word not found
            if i >= m or j >= n or i < 0 or j < 0 or board[i][j] != word[k]:
                return False
            
            # mark visited cell
            board[i][j] = '#'

            # run dfs in all possible directions
            if dfs(i+1, j, k+1) or dfs(i, j+1, k+1) or dfs(i-1, j, k+1) or dfs(i, j-1, k+1):
                return True
            
            # unmark the cell for backtracking
            board[i][j] = word[k]

            return False

        for a in range(m):
            for b in range(n):
                if dfs(a,b,0):
                    return True

        return False
        
        