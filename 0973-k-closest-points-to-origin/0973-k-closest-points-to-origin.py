class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return x**2 + y**2

        maxHeap = []

        for i,j in points:
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, (-dist(i,j), i,j) )
            else:
                heapq.heappushpop(maxHeap, (-dist(i,j), i,j))

        return [[x,y] for h,x,y in maxHeap]       