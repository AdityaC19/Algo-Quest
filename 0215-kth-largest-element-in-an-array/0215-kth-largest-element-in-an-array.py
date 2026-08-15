class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for i in range(len(nums)):
            if len(min_heap) < k:
                heapq.heappush(min_heap, nums[i])
            else:
                heapq.heappushpop(min_heap, nums[i])
        
        return min_heap[0]
        