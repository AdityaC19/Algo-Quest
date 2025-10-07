class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) / 2
        counter = Counter(nums)

        for num in nums:
            if counter[num] > n:
                return num