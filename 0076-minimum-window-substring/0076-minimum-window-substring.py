class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count1 = Counter(t)
        count2 = defaultdict(int)
        req = len(count1)
        formed = 0
        ans = ""
        l = 0 
        minLen = float('inf')

        if len(s) < len(t): return ""

        for r in range(len(s)):
            count2[s[r]] += 1

            if s[r] in count1 and count1[s[r]] == count2[s[r]]:
                formed += 1
            
            while req == formed:
                if (r-l+1) < minLen:
                    ans = s[l:r+1]
                    minLen = (r-l+1)
                
                count2[s[l]] -= 1

                if s[l] in count2 and count2[s[l]] < count1[s[l]]:
                    formed -= 1
                
                l += 1

        return ans

        

        