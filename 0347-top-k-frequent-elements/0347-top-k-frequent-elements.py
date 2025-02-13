import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        h = defaultdict(int)

        for num in nums:
            if num in h:
                h[num] += 1
            else:
                h[num] = 1

        for key, val in h.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (val,key))
            else:
                heapq.heappushpop(min_heap, (val,key))

                    
        return [h[1] for h in min_heap]






            













        