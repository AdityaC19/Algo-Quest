class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        posStk = []
        negStk = []

        ans = []

        for a in asteroids:
            ans.append(a)
            while len(ans) > 1 and ans[-1] < 0 and ans[-2] > 0:
                if abs(ans[-1]) > abs(ans[-2]):
                    ans.pop(-2)
                elif abs(ans[-1]) < abs(ans[-2]):
                    ans.pop(-1)
                else:
                    ans.pop(-2)
                    ans.pop(-1)
        
        return ans



        