import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x):
            return x[0] * x[0] + x[1] * x[1]
        
        n = len(points)
        
        max_heap = []
        res = []

        for point in points:
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-distance(point),point))
            else:
                heapq.heappushpop(max_heap, (-distance(point),point))

        return [h[1] for h in max_heap]


        



