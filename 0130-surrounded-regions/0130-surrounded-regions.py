class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        m, n = len(board), len(board[0])

        q = deque()
        seen = set()

        for i in range(m):
            for j in range(n):
                if i ==0 or j == 0 or i == m-1 or j ==n-1:
                    if board[i][j] == 'O':
                        q.append((i,j))
                        seen.add((i,j))
        
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for r,c in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                    if 0 <= r < m and 0 <= c < n and (r,c) not in seen and board[r][c] == 'O':
                        seen.add((r,c))
                        q.append((r,c))
        
        for i in range(m):
            for j in range(n):
                if (i,j) not in seen and board[i][j] == 'O':
                    board[i][j] = 'X'

