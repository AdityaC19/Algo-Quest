class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l = 0
        r = n-1

        while l <= r:
            x = numbers[l] + numbers[r]
            if x < target:
                l += 1
            elif x > target:
                r -= 1
            else:
                return [l+1,r+1]

        