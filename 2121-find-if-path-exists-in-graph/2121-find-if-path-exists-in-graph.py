class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # 1. DFS with recursion
        # 2. DFS with Stack (iteratively)
        # 3. BFS with deque

        graph = defaultdict(list)

        if source == destination:
            return True

        # Adjacency matrix with dict
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        seen = set()
        seen.add(source)

        q = deque([source])

        while q:
            node = q.popleft()
            if node == destination:
                return True
            for nei_node in graph[node]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    q.append(nei_node)
        return False

        # def dfs(i):
        #     if i == destination:
        #         return True

        #     for nei_node in graph[i]:
        #         if nei_node not in seen:
        #             seen.add(nei_node)
        #             if dfs(nei_node):
        #                 return True
        
        #     return False
        
        #return dfs(source)




