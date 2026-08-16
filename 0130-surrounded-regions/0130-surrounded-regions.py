class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        dont_touch = set()
        q = deque()

        for i in range(m):
            for j in range(n):
                if i ==0 or i == m-1 or j == 0 or j == n-1:
                    if board[i][j] == 'O':
                        dont_touch.add((i, j))
                        q.append((i,j))

        while q:
            i, j = q.popleft()
            for r, c in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                if 0 <= r < m and 0 <= c < n:
                    if (r,c) not in dont_touch and board[r][c] == 'O':
                        q.append((r,c))
                        dont_touch.add((r,c))
    
        for i in range(m):
            for j in range(n):
                if (i,j) not in dont_touch and board[i][j] == 'O':
                    board[i][j] = 'X'


                
        

        

