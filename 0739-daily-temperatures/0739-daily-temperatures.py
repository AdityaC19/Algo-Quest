class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stk = []
        ans = [0] * n

        for i in range(n):
            while stk and temperatures[stk[-1]] < temperatures[i]:
                stk_i = stk.pop()
                ans[stk_i] = i - stk_i

            stk.append(i)
        
        return ans

        