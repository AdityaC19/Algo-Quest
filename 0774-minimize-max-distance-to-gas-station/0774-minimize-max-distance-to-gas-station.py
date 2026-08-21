class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        def penalty(target):
            count = k
            for i in range(1, len(stations)):
                count -= (stations[i] - stations[i-1]) // target
                if count < 0:
                    return False
            return True
        
        l, r = 0, max(stations)
        acc = 10**-6

        while l <= r:
            m = (l+r)/2

            if penalty(m):
                r = m - acc
            else:
                l = m + acc
        
        return l



        