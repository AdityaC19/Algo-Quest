class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indeg = [0] * numCourses

        for u, v in prerequisites:
            graph[v].append(u)
            indeg[u] += 1
        
        q = deque(i for i in range(numCourses) if indeg[i] == 0)
        res = []
        
        while q:
            node = q.popleft()
            res.append(node)
            for nei_node in graph[node]:
                indeg[nei_node] -= 1
                if indeg[nei_node] == 0:
                    q.append(nei_node)
        
        return False if len(res) < numCourses else True


        
        