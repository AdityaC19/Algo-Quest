class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set2 = set(nums2)
        res = set()

        for num in nums1:
            if num in set2:
                res.add(num)
        
        return list(res)




        