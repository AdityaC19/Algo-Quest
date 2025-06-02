class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        min_heap = []

        for num in nums:
            if num in hmap:
                hmap[num] += 1
            else:
                hmap[num] = 1
        
        for key,val in hmap.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (val, key))
            else:
                heapq.heappushpop(min_heap, (val, key))
        
        return [h[1] for h in min_heap]


        