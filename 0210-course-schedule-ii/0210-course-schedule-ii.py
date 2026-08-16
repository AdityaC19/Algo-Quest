class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for u, v in prerequisites:
            graph[u].append(v)
        
        visited = [0] * numCourses
        order = []
        
        def dfs(node):
            if visited[node] == 1:
                return True
            if visited[node] == 2:
                return False
            
            visited[node] = 1

            for nei_node in graph[node]:
                if dfs(nei_node):
                    return True
            
            visited[node] = 2
            order.append(node)
            
            return False
        
        for i in range(numCourses):
            dfs(i)
        
        return order if len(order) == numCourses else []
        



