import heapq
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        min_heap = []

        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, (len(num), num))
            else:
                heapq.heappushpop(min_heap, (len(num), num))
        
        return min_heap[0][1]
        