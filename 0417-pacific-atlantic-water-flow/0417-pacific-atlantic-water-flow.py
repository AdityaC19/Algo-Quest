class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pac_seen = set()
        atl_seen = set()
        
        def bfs(starts, seen):
            q = deque(starts)
            while q:
                for _ in range(len(q)):
                    (i, j) = q.popleft()
                    for r, c in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                        if 0 <= r < m and 0 <= c < n and (r,c) not in seen and heights[r][c] >= heights[i][j]:
                            q.append((r,c))
                            seen.add((r,c))
            
        pac_q = [(i,0) for i in range(m)] + [(0,j) for j in range(n)]
        atl_q = [(i, n-1) for i in range(m)] + [(m-1, j) for j in range(n)]

        for cell in pac_q:
            pac_seen.add(cell)
        for cell in atl_q:
            atl_seen.add(cell)

        bfs(pac_q, pac_seen)
        bfs(atl_q, atl_seen)

        return list(pac_seen & atl_seen)
        #return list(result)
        







        