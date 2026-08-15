class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return x**2 + y**2
        
        max_heap = []
        
        for i,j in points:
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-dist(i,j), i,j))
            else:
                heapq.heappushpop(max_heap, (-dist(i,j), i,j))
        
        print(max_heap)
        
        return [(x,y) for h,x,y in max_heap]
