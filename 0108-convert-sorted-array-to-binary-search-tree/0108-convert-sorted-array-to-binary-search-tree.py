# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def buildTree(subarray, start, end):
            if start > end:
                return None

            mid = (start + end) // 2 

            root = TreeNode(subarray[mid])
            root.left = buildTree(subarray, start, mid-1)
            root.right = buildTree(subarray, mid+1, end)

            return root
        
        return buildTree(nums, 0, len(nums)-1)