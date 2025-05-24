class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indeg = [0] * numCourses

        for u,v in prerequisites:
            graph[v].append(u)
            indeg[u] += 1

        q = deque()

        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        
        order = []
        while q:
            node = q.popleft()
            order.append(node)
            for nei_node in graph[node]:
                indeg[nei_node] -= 1
                if indeg[nei_node] == 0:
                    q.append(nei_node)
        
        return order if len(order) == numCourses else []


