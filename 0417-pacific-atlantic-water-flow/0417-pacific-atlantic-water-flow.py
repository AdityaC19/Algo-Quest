class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pac_q = deque()
        pac_seen = set()

        atl_q = deque()
        atl_seen = set()

        for i in range(n):
            pac_q.append((0,i))
            pac_seen.add((0,i))
        
        for i in range(m):
            pac_q.append((i,0))
            pac_seen.add((i,0))
        
        for i in range(n):
            atl_q.append((m-1,i))
            atl_seen.add((m-1,i))
        
        for i in range(m):
            atl_q.append((i,n-1))
            atl_seen.add((i,n-1))
        
        def bfs(q, seen):
            while q:
                for _ in range(len(q)):
                    (i, j) = q.popleft()
                    for r,c in [(i, j+1), (i+1, j), (i-1, j), (i, j-1)]:
                        if 0 <= r < m and 0 <= c < n and heights[r][c] >= heights[i][j] and (r,c) not in seen:
                            q.append((r,c))
                            seen.add((r,c))
        
        bfs(pac_q, pac_seen)
        bfs(atl_q, atl_seen)
        
        return list(pac_seen & atl_seen)

                     

        