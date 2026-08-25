class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        seen = set()
        seen.add(source)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node):
            # if not node:
            #     return False
            
            if node == destination:
                return True
            
            seen.add(node)
            
            for nei_node in graph[node]:
                if nei_node not in seen:
                    if dfs(nei_node):
                        return True
            
            return False
        
        return dfs(source)



        