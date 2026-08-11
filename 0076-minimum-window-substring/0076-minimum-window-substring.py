class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1 = len(s)
        n2 = len(t)
        count1 = Counter(t)
        count2 = defaultdict(int)
        req = len(count1)
        formed = 0
        l, r = 0, 0
        ans = ""
        res = float('inf')

        if n1 < n2:
            return ""

        for r in range(n1):
            count2[s[r]] += 1

            if s[r] in count1 and count2[s[r]] == count1[s[r]]:
                formed += 1
            
            while req == formed:
                if (r-l+1) < res:
                    ans = s[l:r+1]
                    res = r-l+1

                count2[s[l]] -= 1

                if s[l] in count1 and count2[s[l]] < count1[s[l]]:
                    formed -= 1
                l += 1
            
        return ans
            






            
            
                
            


