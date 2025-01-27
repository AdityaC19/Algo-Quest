class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for u, v in prerequisites:
            graph[u].append(v)
        
        print(graph)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses
        ans = []

        def dfs(i):
            state = states[i]
            if state == VISITED: return True # verified
            elif state == VISITING: return False # in loop

            states[i] = VISITING

            for nei_node in graph[i]:    
                if not dfs(nei_node):   # in loop
                    return False

            states[i] = VISITED
            ans.append(i) # append the node once its verified
            return True  
        
            
        # for i in range(numCourses):
        #     if dfs(i):
        #         pass
        # return ans
        
        #shorthand version of above 
        return ans if all(dfs(i) for i in range(numCourses)) else []

        
        
        