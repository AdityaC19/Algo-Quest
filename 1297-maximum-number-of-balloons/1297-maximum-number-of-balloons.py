class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        h = defaultdict(int)
        balloon = 'balloon'

        for i in text:
            if i in balloon:
                h[i] += 1
        
        return min(h['b'],h['a'],h['l']//2,h['o']//2,h['n'],)
        



        
        return c
            
                


            

