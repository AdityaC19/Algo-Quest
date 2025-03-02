class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        q = deque()
        #safe = set()

        # Mark Os at the boudary (marking as #)
        for i in range(m):
            for j in [0, n-1]:  # First and last columns
                if board[i][j] == 'O':
                    board[i][j] = "#"
                    q.append((i, j))
                    #safe.add((i, j))

        for j in range(n):
            for i in [0, m-1]:  # First and last rows
                if board[i][j] == 'O':
                    board[i][j] = "#"
                    q.append((i, j))
                    #safe.add((i, j))
        
        # Perform BFS to mark boundary reachable Os as safe (marking as #)
        while q:
            # for _ in range(len(q)):   # level wise traveral is not needed so need for loop
            i, j = q.popleft()
            for r, c in [(i+1, j), (i, j+1), (i, j-1), (i-1, j)]:
                if 0 <= r < m and 0 <= c < n and board[r][c] == "O":
                    board[r][c] = "#"
                    q.append((r,c))
                    #safe.add((r,c))
        
        # Mark all remaining O to X and turn # to O
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "#":
                    board[i][j] = "O"
                    

                    
                    





        