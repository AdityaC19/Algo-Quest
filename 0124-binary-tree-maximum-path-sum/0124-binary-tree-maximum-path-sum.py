# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        largest_sum = [float('-inf')]

        def optimal_path(root):
            if not root:
                return 0

            left_sum = max(0, optimal_path(root.left))
            right_sum = max(0, optimal_path(root.right))
            summ = left_sum + right_sum + root.val
            largest_sum[0] = max(largest_sum[0], summ)

            return root.val + max(left_sum, right_sum)
        
        optimal_path(root)
        return largest_sum[0] 
        