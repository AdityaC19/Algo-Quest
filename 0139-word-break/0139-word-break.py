class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        memo = {}

        def dfs(l):
            if l == n:
                return True 
            
            if l in memo:
                return memo[l]

            for r in range(l, n + 1):
                if s[l:r] in word_set:
                    if dfs(r):  
                        memo[l] = True  
                        return True
            
            memo[l] = False
            
            return False 

        return dfs(0)

        # while l <= r:
        #     if s[l:r] in wordDict:
        #         ans.append(s[l:r])
        #         print(ans)
        #         l = r
        #         r = n
        #     else:
        #         r -= 1
        
        # return True if ''.join(ans) == s else False
            
        
        


        



        