# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = []
        def inOrder(root):
            if not root:
                return 0

            left = inOrder(root.left)
            ans.append(root.val)
            right = inOrder(root.right)

        
        inOrder(root)

        min_diff = float('inf')
        for i in range(len(ans)-1):
            min_diff = min(min_diff, abs(ans[i]- ans[i+1]))
            
        return min_diff






