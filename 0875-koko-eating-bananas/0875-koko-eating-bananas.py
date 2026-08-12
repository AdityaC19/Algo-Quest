class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_speed(k: int):
            hours = 0
            for pile in piles:
                hours += ceil (pile/k)
            
            return hours <= h
        
        l = 1
        r = max(piles)

        while l < r:
            k = l + (r-l)//2

            if k_speed(k):
                r = k
            else:
                l = k+1
        
        return l


            

        