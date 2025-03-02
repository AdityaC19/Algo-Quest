class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = defaultdict(list)
        seen = set()

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] != 0 and i != j: 
                    graph[i].append(j)


        def dfs(i):
            seen.add(i)
            
            for nei in graph[i]:
                if nei not in seen:
                    dfs(nei)
        
        count = 0
        for i in range(n):
            if i not in seen:
                count += 1
                dfs(i)
        
        return count

            


        

        