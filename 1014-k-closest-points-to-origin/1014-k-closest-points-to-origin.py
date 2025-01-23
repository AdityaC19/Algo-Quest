import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x):
            return x[0] * x[0] + x[1] * x[1]
        
        min_heap = []
        res = []

        for point in points:
            heapq.heappush(min_heap, (distance(point),point))
            
        print(min_heap)
        res = []

        while k:
            res.append(heapq.heappop(min_heap))
            k-=1

        return [h[1] for h in res]


        



