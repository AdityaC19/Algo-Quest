class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for u, v in prerequisites:
            graph[u].append(v)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses

        def dfs(i):
            state = states[i]
            if state == VISITED: return True
            elif state == VISITING: return False

            states[i] = VISITING

            for nei_node in graph[i]:    
                if not dfs(nei_node):
                    return False

            states[i] = VISITED
            return True  
        
            
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
        
        
    