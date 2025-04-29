class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for u, v in prerequisites:
            graph[u].append(v)
        
        visited = [False] * numCourses
        path_visited = [False] * numCourses

        def dfs(node):
            if visited[node]: return False
            elif path_visited[node]: return True

            visited[node] = True
            path_visited[node] = True

            for nei_node in graph[node]:
                if dfs(nei_node):
                    return True
                elif path_visited[nei_node]:
                    return True
            
            path_visited[node] = False
            return False
        
        for i in range(numCourses):
            if not visited[i]:
                if dfs(i):
                    return False
        
        return True
            

            
                    