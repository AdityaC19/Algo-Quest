class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pseen = set()
        aseen = set()
        m, n = len(heights), len(heights[0])

        # left + top
        pac = deque([(i, 0) for i in range(m)] + [(0, j) for j in range(n)])
        # right + bottom
        atl = deque([(i, n-1) for i in range(m)] + [(m-1, j) for j in range(n)])

        pseen = set(pac)
        aseen = set(atl)

        def bfs(q, seen):
            while q:
                for _ in range(len(q)):
                    (i,j) = q.popleft()
                    for r, c in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                        if 0 <= r < m and 0 <= c < n and (r,c) not in seen and heights[r][c] >= heights[i][j]:
                            q.append((r,c))
                            seen.add((r,c))
        
        bfs(pac, pseen)
        bfs(atl, aseen)
        return list(pseen & aseen)



        