class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        counter = Counter(nums)

        for i in nums:
            if counter[i] > n//2:
                return i