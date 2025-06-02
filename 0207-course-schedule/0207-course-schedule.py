class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for u, v in prerequisites:
            graph[u].append(v)

        visited = [0] * numCourses

        def dfs(i):
            if visited[i] == 1: return True
            if visited[i] == 2: return False

            visited[i] = 1

            for nei_node in graph[i]:
                if dfs(nei_node):
                    return True
            
            visited[i] = 2
            return False
        
        for i in range(numCourses):
            if not visited[i]:
                if dfs(i):
                    return False
        return True