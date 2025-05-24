class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        seen = set()
        seen.add(source)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(i):
            if i == destination:
                return True
            
            for nei_node in graph[i]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    if dfs(nei_node):
                        return True
            return False
        
        return dfs(source)
        

