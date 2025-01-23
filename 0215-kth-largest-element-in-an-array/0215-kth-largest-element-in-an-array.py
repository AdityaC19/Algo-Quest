import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] = -nums[i]
        
        heapq.heapify(nums)

        res = [0] * n
        for i in range(n):
            minn = heapq.heappop(nums)
            res[i] = minn
        
        return -res[k-1]
        
        


        