import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        hmap = Counter(nums)

        for key, val in hmap.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (val, key))
            else:
                heapq.heappushpop(min_heap, (val, key))
        
        return [hmap[1] for hmap in min_heap]
            






 





            













        