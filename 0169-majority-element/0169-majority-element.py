class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        n = len(nums)

        for key,val in counter.items():
            if val > (n//2):
                return key
        