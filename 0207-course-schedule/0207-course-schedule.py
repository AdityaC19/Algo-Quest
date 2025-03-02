from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        n = numCourses
        indeg = [0] * n

        for u,v in prerequisites:
            graph[v].append(u)
            indeg[u] += 1
        
        q = deque()

        for i in range(n):
            if indeg[i] == 0:
                q.append(i)
        
        order = []
        
        while q:
            node = q.popleft()
            order.append(node)

            for nei in graph[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)

        if len(order) < n:
            return False
        return True


        