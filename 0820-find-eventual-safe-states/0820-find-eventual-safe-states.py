class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        g = defaultdict(list)

        for u, nei in enumerate(graph):
            for v in nei:
                g[u].append(v)
        
        print(g)
        
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * len(graph)
        ans = []

        def dfs(i):
            state = states[i]
            if state == VISITED: return True
            elif state == VISITING: return False

            states[i] = VISITING

            for nei_node in g[i]:
                if not dfs(nei_node):
                    return False
            
            states[i] = VISITED
            return True
        
        for i in range(len(graph)):
            if dfs(i):
                ans.append(i) 
        
        return ans





        

        