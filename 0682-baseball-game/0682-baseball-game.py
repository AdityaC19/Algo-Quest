class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        ans = 0

        for i in operations:
            if i == '+':
                summ = int(res[-1]) + int(res[-2])
                res.append(summ)
            elif i == 'D':
                double = int(res[-1])*2
                res.append(double)
            elif i == 'C':
                res.pop()
            else:
                res.append(int(i))
        
        return sum(res)
                

        