from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        n = numCourses
        indegree = [0] * n

        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1

        q = deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        
        topo = []

        while q:
            node = q.popleft()
            topo.append(node)
            for nei_node in graph[node]:
                indegree[nei_node] -= 1
                if indegree[nei_node] == 0:
                    q.append(nei_node)
        
        if len(topo) == n:
            return topo
        else:
            return []


       