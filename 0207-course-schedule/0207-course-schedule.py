class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for u, v in prerequisites:
            graph[u].append(v)
        
        visited = [0] * numCourses
        #path_visited = [False] * numCourses

        def dfs(node):
            if visited[node] == 2: return False
            elif visited[node] == 1: return True

            visited[node] = 1
            #path_visited[node] = True

            for nei_node in graph[node]:
                if dfs(nei_node):
                    return True

            
            visited[node] = 2
            return False
        
        for i in range(numCourses):
            if not visited[i]:
                if dfs(i):
                    return False
        
        return True
            

            
                    