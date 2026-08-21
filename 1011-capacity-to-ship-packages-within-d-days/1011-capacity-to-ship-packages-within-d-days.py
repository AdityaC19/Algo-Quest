class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)

        def helper(max_sum):
            d = 1
            cur_sum = 0
            for w in weights:
                cur_sum += w
                if cur_sum > max_sum:
                    d += 1
                    cur_sum = w
                    if d > days:
                        return False
            return True

        l , r = max(weights), sum(weights)
        ans = r

        while l <= r:
            m = (l+r)//2
            if helper(m):
                ans = m
                r = m -1
            else:
                l = m + 1
        
        return l

        