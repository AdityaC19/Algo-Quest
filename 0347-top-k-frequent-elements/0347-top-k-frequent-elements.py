class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = defaultdict(int)
        min_heap = []

        for i in range(len(nums)):
            hmap[nums[i]] += 1

        for key, value in hmap.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (value, key)) 
            else:
                heapq.heappushpop(min_heap, (value, key))
        
        return [h[1] for h in min_heap]
        