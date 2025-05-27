class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
  
        max_len = max(len(word) for word in wordDict)
        word_set = set(wordDict)

        for i in range(1, n+1):
            for j in range(max(0, i - max_len), i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]

        # while l <= r:
        #     if s[l:r] in wordDict:
        #         ans.append(s[l:r])
        #         print(ans)
        #         l = r
        #         r = n
        #     else:
        #         r -= 1
        
        # return True if ''.join(ans) == s else False
            
        
        


        



        