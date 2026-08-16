class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        m , n = len(grid), len(grid[0])
        seen = set()
        time = 0
        fresh_oranges = 0

        # multi-source BFS
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                    seen.add((i,j))
                if grid[i][j] == 1:
                    fresh_oranges += 1
        
        if fresh_oranges == 0: return 0
        while q:
            time += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for r, c in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                    if 0 <= r < m and 0 <= c < n and (r,c) not in seen and grid[r][c] == 1:
                        grid[r][c] = 2
                        fresh_oranges -= 1
                        q.append((r,c))
                        seen.add((r,c))
                if fresh_oranges == 0:
                    return time

        return -1
                





        