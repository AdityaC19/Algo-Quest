class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            m = l + ((r-l)//2)

            sum = 0
            for pile in piles:
                sum += ceil(pile / m)
            
            if sum <= h:
                r = m
            else:
                l = m + 1
        return l
        

        