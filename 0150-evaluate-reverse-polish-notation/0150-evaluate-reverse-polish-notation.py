class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        signs = ('+', '-', '*', '/')
        stk = []
        
        for i in tokens:
            if i in '+-*/':
                b, a = stk.pop(), stk.pop()
                res = str(int(eval(a + i + b)))
                stk.append(res)
            else:
                stk.append(i)
        
        return int(stk[0])
