class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        m, n = len(rooms), len(rooms[0])

        q = deque()
        seen = set()
        empty = 0

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i,j))
                    seen.add((i,j))
        
        count =0
        while q:
            count += 1
            for _ in range(len(q)):
                i,j = q.popleft()
                for r, c in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                    if 0 <= r < m and 0 <= c < n and (r,c) not in seen and rooms[r][c] == 2147483647 :
                        rooms[r][c] = count
                        q.append((r, c))
                        seen.add((r,c))
                

        