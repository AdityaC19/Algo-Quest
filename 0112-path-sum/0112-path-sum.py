# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(root, currSum):
            if not root:
                return False
            
            currSum += root.val

            if not root.left and not root.right:
                return currSum == targetSum

            # if currSum == targetSum:
            #     return True
            
            return helper(root.left, currSum) or helper(root.right, currSum)
             
        
        return helper(root, 0)
        
        