class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for u,v in invocations:
            graph[u].append(v)
        
        seen = set()
        
        def dfs(node):
            seen.add(node)

            for nei_node in graph[node]:
                if nei_node not in seen:
                    dfs(nei_node)
        
        dfs(k)

        ans = []
        for i in range(n):
            if i in seen:
                continue
            
            for nei in graph[i]:
                if nei in seen:
                    return list(range(n))
            
            ans.append(i)
        
        return ans



            

        