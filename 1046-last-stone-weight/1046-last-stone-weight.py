class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)

        for i in range(n):
            stones[i] = -stones[i]
        
        heapq.heapify(stones)

        while len(stones) > 1:
            largest = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if largest != second:
                heapq.heappush(stones, largest - second)
            
        if len(stones) == 1:
            return -stones[0]
        else:
            return 0
        