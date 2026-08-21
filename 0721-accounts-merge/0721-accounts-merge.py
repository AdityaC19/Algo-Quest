class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        seen = set()
        ans = []

        for account in accounts:
            for email in account[1:]:
                graph[email].add(account[1])
                graph[account[1]].add(email)
        
        def dfs(node, res):
            if node in seen:
                return 
            
            seen.add(node)

            for nei_node in graph[node]:
                if nei_node not in seen:
                    dfs(nei_node, res)
            
            res.append(node)
        
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in seen:
                    res = []
                    dfs(email, res)
                    if res:
                        ans.append([name] + sorted(res))
        
        return ans

        