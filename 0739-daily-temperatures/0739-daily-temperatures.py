class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stk = []    #(idx, temp)
        ans = [0] * n

        for i in range(n):
            while stk and temperatures[i] > stk[-1][1]:
                stk_i, stk_temp = stk.pop()
                ans[stk_i] = i - stk_i

            stk.append((i, temperatures[i]))
        
        return ans
        