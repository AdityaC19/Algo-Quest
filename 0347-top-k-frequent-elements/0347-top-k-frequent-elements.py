class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        min_heap = []

        for key, val in counter.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (val, key))
            else:
                heapq.heappushpop(min_heap, (val, key))
        
        return [h[1] for h in min_heap]
        