class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        g = defaultdict(list)

        for u, nei in enumerate(graph):
            for v in nei:
                g[u].append(v)
        
        VISITING, VISITED = 1, 2
        states = [0] * len(graph)
        safe_nodes = []

        def dfs(i):
            if states[i] == VISITING: return False
            elif states[i] == VISITED: return True

            states[i] = VISITING

            for nei in g[i]:
                if not dfs(nei):
                    return False
            
            states[i] = VISITED
            #safe_nodes.append(i)
            return True
        
        for i in range(len(graph)):
            if dfs(i):
                safe_nodes.append(i)
        
        return safe_nodes
        