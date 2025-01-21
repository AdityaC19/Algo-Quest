# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        decision = [True]

        def height(root):
            if not root:
                return 0
            
            left = height(root.left)
            right = height(root.right)
            diff = abs(left - right)
            
            if diff > 1:
                decision[0] = False
                return 0
            
            return 1 + max(left,right)
            
        height(root)
        return decision[0]

        
        