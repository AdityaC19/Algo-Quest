class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for u, v in sorted(tickets, reverse = True):
            graph[u].append(v)

        
        itinerary = []
        
        def dfs(node):
            while graph[node]:
                dfs(graph[node].pop())
            itinerary.append(node)
        
        dfs('JFK')
        
        return itinerary [::-1]
