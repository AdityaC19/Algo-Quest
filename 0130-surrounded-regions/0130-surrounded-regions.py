class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        q = deque()
        safe = set()

        # Mark all boundary O as safe:
        for i in range(m):
            for j in [0, n-1]:  # first and last col
                if board[i][j] == 'O':
                    q.append((i,j))
                    safe.add((i,j))
        
        for i in [0, m-1]:  # First and last row
            for j in range(n):
                if board[i][j] == 'O':
                    q.append((i,j))
                    safe.add((i,j))
        
        # Use BFS to mark safe Os
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for r, c in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                    if 0 <= r < m and 0 <= c < n and board[r][c] == 'O' and (r,c) not in safe :
                        q.append((r,c))
                        safe.add((r,c))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i,j) not in safe:
                    board[i][j] = 'X'
        





        