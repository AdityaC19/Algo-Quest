class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        formed = 0
        count1 = Counter(t)
        count2 = defaultdict(int)
        req = len(count1)
        ans = float('inf')
        res = ""
        l = 0
        r = 0



        for r in range(n):
            count2[s[r]] += 1

            if s[r] in count1 and count1[s[r]] == count2[s[r]]:
                formed += 1
            
            while formed == req:
                if (r-l+1) < ans:
                    res = s[l:r+1]
                    ans = (r-l+1)
                
                count2[s[l]] -= 1

                if s[l] in count1 and count2[s[l]] < count1[s[l]]:
                    formed -=1 
                l+=1

        return res 



        


        