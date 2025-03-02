class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for u, v in prerequisites:
            graph[u].append(v)
        
        visited = [False] * numCourses
        path_visited = [False] * numCourses

        def dfs(node):
            if path_visited[node]:    # Cycle detected
                return True
            elif visited[node]:       # ALready checked, no cycle
                return False

            visited[node] = True
            path_visited[node] = True 

            for nei in graph[node]:
                #if not visited[nei]:
                if dfs(nei):    # if cycle detected, propogate up
                    return True
            
            path_visited[node] = False  # backtrack
            return False
        
        for i in range(numCourses):
            if not visited[i]:
                if dfs(i):
                    return False
        
        return True
        