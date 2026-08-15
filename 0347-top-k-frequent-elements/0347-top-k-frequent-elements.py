class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        n = len(nums)
        bucket = [0] * (n+1)

        for i, freq in counter.items():
            if bucket[freq] == 0:
                bucket[freq] = [i]
            else:
                bucket[freq].append(i)
        
        res = []
        for i in range(n, -1, -1):
            if bucket[i] != 0:
                res.extend(bucket[i])
            if len(res) == k:
                return res
        

        # counter = Counter(nums)

        # min_heap = []

        # for key, val in counter.items():
        #     if len(min_heap) < k:
        #         heapq.heappush(min_heap, (val, key))
        #     else:
        #         heapq.heappushpop(min_heap, (val, key))
        
        # return [h[1] for h in min_heap]
        