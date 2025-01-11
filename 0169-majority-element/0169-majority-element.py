class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        h = defaultdict(int)
        
        for i in nums:
            h[i] +=1

        for i in nums:
            if h[i] > n//2:
                return i