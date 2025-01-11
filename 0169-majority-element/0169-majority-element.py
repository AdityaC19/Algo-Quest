class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        h = defaultdict(int)
        
        for i in nums:
            h[i] +=1

        return max(h, key=h.get)