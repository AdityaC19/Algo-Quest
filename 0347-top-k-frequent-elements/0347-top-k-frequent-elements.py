class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counter = Counter(nums)
        bucket = [0] * (n+1)

        for key, freq in counter.items():
            if bucket[freq] == 0:
                bucket[freq] = [key]
            else:
                bucket[freq].append(key)
        
        ans = []

        for i in range(n, -1, -1):
            if bucket[i] != 0:
                ans.extend(bucket[i])
            if len(ans) == k:
                return ans
        
        


        # hmap = defaultdict(int)
        # min_heap = []

        # for i in range(len(nums)):
        #     hmap[nums[i]] += 1

        # for key, value in hmap.items():
        #     if len(min_heap) < k:
        #         heapq.heappush(min_heap, (value, key)) 
        #     else:
        #         heapq.heappushpop(min_heap, (value, key))
        
        # return [h[1] for h in min_heap]
        