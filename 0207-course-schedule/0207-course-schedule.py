class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indeg = [0] * numCourses

        for u, v in prerequisites:
            graph[v].append(u)
            indeg[u] += 1
        
        q = deque([i for i in range(numCourses) if indeg[i] == 0])
        res = []

        while q:
            node = q.popleft()
            res.append(node)
            for nei_node in graph[node]:
                indeg[nei_node] -= 1
                if indeg[nei_node] == 0:
                    q.append(nei_node)
        
        return True if len(res) == numCourses else False
        

        

        # visited = [0] * numCourses

        # def dfs(i):
        #     if visited[i] == 1: return True
        #     if visited[i] == 2: return False

        #     visited[i] = 1

        #     for nei_node in graph[i]:
        #         if dfs(nei_node):
        #             return True
            
        #     visited[i] = 2
        #     return False
        
        # for i in range(numCourses):
        #     if not visited[i]:
        #         if dfs(i):
        #             return False
        # return True