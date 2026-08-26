class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        hmap = defaultdict(int)

        for i in range(n):
            hmap[nums[i]] += 1
        
        min_heap = []

        for key, val in hmap.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (val, key))
            else:
                heapq.heappushpop(min_heap, (val, key))

        return [h[1] for h in min_heap]

        


