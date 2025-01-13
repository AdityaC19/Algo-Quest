class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        n = len(nums1)
        m = len(nums2)

        for i in range(n):
            for j in range(m):
                if nums1[i] == nums2[j]:
                    for k in range(j+1,m):
                        if nums2[k] > nums1[i]:
                            ans.append(nums2[k])
                            break
                    else:
                        ans.append(-1)
                    break
        
        return ans
        

        