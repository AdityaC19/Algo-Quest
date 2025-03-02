class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        seen = set()

        def bfs(i):
            q = deque([i])
            while q:
                node = q.popleft()

                for nei in range(n):
                    if isConnected[node][nei] == 1 and nei not in seen:
                        q.append(nei)
                        seen.add(nei)
        
        count = 0

        for i in range(n):
            if i not in seen:
                count += 1
                bfs(i)
                seen.add(i)
        
        return count



