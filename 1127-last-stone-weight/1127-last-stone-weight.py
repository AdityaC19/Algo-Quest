import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)

        for i in range(n):
            stones[i] = -stones[i]
        
        heapq.heapify(stones)

        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)

            heapq.heappush(stones, s1-s2)
        
        if len(stones) == 1:
            return -heapq.heappop(stones)
        else:
            return 0
        

        