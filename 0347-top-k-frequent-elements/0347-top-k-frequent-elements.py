import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        h = Counter(nums)

        for key,val in h.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (val,key))
            else:
                heapq.heappushpop(min_heap, (val,key))
        
        return [h[1] for h in min_heap]
            
        
   
        # for i in range(len(nums)):
        #     if nums[i] in h:
        #         h[nums[i]] += 1
        #     else:
        #         h[nums[i]] = 1
        

        
        # top_k = [key for key, _ in heapq.nlargest(k, h.items(), key=lambda x: x[1])]

        # return top_k


