class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        rank = [0] * (n+1)

        def find(node):
            if node == parent[node]:    # this is the root parent
                return node
            parent[node] = find(parent[node])   # Path compression
            return parent[node]

        
        def union(u, v):
            root_u = find(u)
            root_v = find(v)

            if root_u == root_v:
                return False        # Cycle detected (redundant edge)
            
            if rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            elif rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            else:
                parent[root_v] = root_u
                rank[root_u] += 1
            
            return True             # Union successful
        
        for u, v in edges:
            if not union(u,v):
                return [u,v]        # First edge that forms a cycle
        
        return []          # No redundant edge found
        
