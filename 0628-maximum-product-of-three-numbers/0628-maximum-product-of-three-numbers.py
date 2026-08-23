class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max_heap = []
        min_heap = []

        for num in nums:
            if len(min_heap) < 3:
                heapq.heappush(min_heap, num)
            else:
                heapq.heappushpop(min_heap, num)
        
        for num in nums:
            if len(max_heap) < 2:
                heapq.heappush(max_heap, -num)
            else:
                heapq.heappushpop(max_heap, -num)
                
        res1 = min_heap[0] * min_heap[1] * min_heap[2]
        res2 = max_heap[0] * max_heap[1] * max(min_heap)
        return max(res1, res2)
        