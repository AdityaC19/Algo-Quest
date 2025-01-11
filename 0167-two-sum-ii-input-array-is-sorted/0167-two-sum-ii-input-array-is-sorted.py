class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers)-1

        while L <= R:
            x = numbers[R] + numbers[L]
            if x == target:
                return [L+1,R+1]
            elif x < target:
                L += 1
            else:
                R-=1

        



