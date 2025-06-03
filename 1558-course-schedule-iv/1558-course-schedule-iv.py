class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)

        for u, v in prerequisites:
            graph[u].append(v)

        pre = [set() for _ in range(numCourses)]

        visited = [False] * numCourses

        def dfs(node):
            if visited[node]:
                return pre[node]
            visited[node] = True
            for nei in graph[node]:
                pre[node].add(nei)
                pre[node].update(dfs(nei))
            return pre[node]

        for i in range(numCourses):
            dfs(i)

        res = []    
        for q in queries:
            i, j = q
            res.append(j in pre[i])
        
        return res

 
            


