class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for u, v in prerequisites:
            graph[u].append(v)
        
        visited = [0] * numCourses
        

        # DFS to detect cycle
        def dfs(i):
            if visited[i] == 1:  # cycle detected
                return True
            if visited[i] == 2:
                return False
            
            visited[i] = 1

            for nei in graph[i]:
                if dfs(nei):
                    return True
            
            visited[i] = 2
            return False
        
        for i in range(numCourses):
            if dfs(i):
                return False
        
        return True
