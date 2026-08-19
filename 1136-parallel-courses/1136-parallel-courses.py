class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = defaultdict(list)
        indeg = [0] * (n+1)

        for u, v in relations:
            graph[u].append(v)
            indeg[v] += 1
        
        q = deque()
        
        for i in range(1, n+1):
            if indeg[i] == 0:
                q.append(i)
        
        order = []
        res = 0
        while q:
            res += 1
            for _ in range(len(q)):
                node = q.popleft()
                order.append(node)
                for nei_node in graph[node]:
                    indeg[nei_node] -= 1
                    if indeg[nei_node] == 0:
                        q.append(nei_node)
        
        return res if len(order) == n else -1
