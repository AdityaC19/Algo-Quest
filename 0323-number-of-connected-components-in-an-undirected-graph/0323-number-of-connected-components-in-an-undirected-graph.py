class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        seen = set()

        def dfs(node):
            seen.add(node)
            
            for nei_node in graph[node]:
                if nei_node not in seen:
                    dfs(nei_node)
                    
        comp = 0

        for i in range(n):
            if i not in seen:
                dfs(i)
                comp += 1
        
        return comp


        