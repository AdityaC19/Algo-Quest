class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for u,v in prerequisites:
            graph[u].append(v)

        UNVISITED, VISITING, VISITED = 0, 1, 2
        cache = [UNVISITED] * numCourses
        order = []

        def dfs(i):
            state = cache[i]
            if state == VISITING: return False
            elif state == VISITED: return True

            cache[i] = VISITING

            for nei_node in graph[i]:
                if not dfs(nei_node):
                    return False
            
            cache[i] = VISITED
            order.append(i)
            return True
            
        
        for node in range(numCourses):
            if not dfs(node):
                return []
        
        return order


