class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        l, r =0, 0
        maxLen = 0
        hmap = defaultdict(int)

        for r in range(n):
            hmap[fruits[r]] += 1

            while len(hmap) > 2:
                hmap[fruits[l]] -= 1
                if hmap[fruits[l]] == 0:
                    del hmap[fruits[l]]
                l = l + 1

            maxLen = max(maxLen, (r-l+1))
        
        return maxLen




