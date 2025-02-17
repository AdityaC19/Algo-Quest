# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def buildTree(subarray):
            if not subarray:
                return None

            mid = len(subarray) // 2 

            root = TreeNode(subarray[mid])
            root.left = buildTree(subarray[:mid])
            root.right = buildTree(subarray[mid+1:])

            return root
        
        return buildTree(nums)