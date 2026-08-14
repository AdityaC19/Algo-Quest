class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures
        stk = []
        n = len(temp)
        ans = [0] * n

        for i, t in enumerate(temp):
            while stk and t > stk[-1][1]:
                stk_i, stk_t = stk.pop()
                ans[stk_i] = i - stk_i
            
            stk.append((i, t))
        
        return ans



        