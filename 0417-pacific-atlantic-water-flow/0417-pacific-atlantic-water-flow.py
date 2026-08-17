class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacq = deque()
        atlq = deque()

        pseen = set()
        aseen = set()

        m, n = len(heights), len(heights[0])
        # left + top
        pacq = deque([(i,0) for i in range(m)] + [(0, j) for j in range(n)])
        # right + bottom
        atlq = deque([(i, n-1) for i in range(m)] + [(m-1, j) for j in range(n)])

        pseen = set(pacq)
        aseen = set(atlq)

        def bfs(q, seen):
            while q:
                i, j = q.popleft()
                for r,c in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                    if 0 <= r < m and 0 <= c < n and (r,c) not in seen and heights[r][c] >= heights[i][j]:
                        q.append((r,c))
                        seen.add((r,c))
        
        bfs(pacq, pseen)
        bfs(atlq, aseen)

        return list(pseen & aseen)



