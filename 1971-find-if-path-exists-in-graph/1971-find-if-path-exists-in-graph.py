class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        q = deque([source])
        seen = set()
        seen.add(source)

        if source ==destination:
            return True

        while q:
            node = q.popleft()

            if node == destination:
                return True
                
            for nei_node in graph[node]:
                if nei_node not in seen:
                    q.append(nei_node)
                    seen.add(nei_node)
        
        return False

