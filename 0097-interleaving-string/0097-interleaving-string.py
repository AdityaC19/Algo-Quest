class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        dp = [[False] * (n+1) for _ in range(m+1)]

        dp[m][n] = True

        if m + n != len(s3):
            return False

        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                
                if j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True
        
        return dp[0][0]
                    









        # memo = {}

        # def dfs(i, j):
        #     if i == len(s1) and j == len(s2):
        #         return True
            
        #     if (i,j) in memo:
        #         return memo[(i,j)]
            
        #     if i < len(s1) and s1[i] == s3[i+j]:
        #         if dfs(i+1, j):
        #             return True
            
        #     if j < len(s2) and s2[j] == s3[i+j]:
        #         if dfs(i, j+1):
        #             return True
            
        #     memo[(i, j)] = False
            
        #     return memo[(i, j)]
        
        # if len(s1) + len(s2) != len(s3):
        #     return False

        # return dfs(0,0)

        
        