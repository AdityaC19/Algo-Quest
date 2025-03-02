class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        q = deque()
        safe = set()

        # Mark Os at the boudary
        for i in range(m):
            for j in [0, n-1]:  # First and last columns
                if board[i][j] == 'O':
                    q.append((i, j))
                    safe.add((i, j))

        for j in range(n):
            for i in [0, m-1]:  # First and last rows
                if board[i][j] == 'O':
                    q.append((i, j))
                    safe.add((i, j))
        
        # Perform BFS to mark boundary reachable Os as safe (i.e. add to safe set)
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for r, c in [(i+1, j), (i, j+1), (i, j-1), (i-1, j)]:
                    if 0 <= r < m and 0 <= c < n and board[r][c] == "O" and (r,c) not in safe:
                        q.append((r,c))
                        safe.add((r,c))
        
        # Mark all the O to X which are not in safe set
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i,j) not in safe:
                    board[i][j] = "X"
                    

                    
                    





        