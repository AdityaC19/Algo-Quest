class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        print(merged)

        n = len(merged)
        print(n)

        mid = math.floor(n / 2)
        print(merged[mid])

        if n % 2 == 0:
            median = (merged[mid] + merged[mid-1]) / 2            
        else:
            median = (merged[mid]) 
        
        return median
