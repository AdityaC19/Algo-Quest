class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Make parent and rank lists
        n = len(edges)
        parent = [i for i in range(n+1)]
        rank = [0] * (n+1)

        def find(node):
            if node == parent[node]:
                return parent[node]
            parent[node] = find(parent[node])   # path compression
            return parent[node]
        
        def union(u, v):
            rootU, rootV = find(u), find(v)
            if rootU == rootV:
                return False
            
            # if rank[rootU] > rank[rootV]: rootU will become parent of rootV
            if rank[rootU] > rank[rootV]:   
                parent[rootV] = rootU
                rank[rootU] += rank[rootV]
            else:
                parent[rootU] = rootV
                rank[rootV] += rank[rootU]
            
            return True
        
        for u, v in edges:
            if not union(u,v):
                return [u,v]
        return []


            
        