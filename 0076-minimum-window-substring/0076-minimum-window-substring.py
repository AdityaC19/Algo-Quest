class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""

        count_s = defaultdict(int)
        count_t = Counter(t)
        req = len(count_t)
        formed = 0
        ans = ""
        l, r= 0, 0
        minLen = float('inf')

        for r in range(len(s)):
            count_s[s[r]] += 1

            if s[r] in count_t and count_s[s[r]] == count_t[s[r]]:
                formed += 1

            while req == formed:
                if (r-l+1) < minLen:
                    ans = s[l:r+1]
                    minLen = min(minLen, (r-l+1))
                
                count_s[s[l]] -= 1
                
                if s[l] in count_t and count_s[s[l]] < count_t[s[l]]:
                    formed -= 1
                
                l += 1
        
        return ans