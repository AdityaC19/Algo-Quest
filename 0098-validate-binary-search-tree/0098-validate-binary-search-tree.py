# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []
        def helper(node):
            if not node:
                return 0
            
            left = helper(node.left)
            ans.append(node.val)
            right = helper(node.right)

        helper(root)

        if ans == sorted(ans) and len(set(ans)) == len(ans):
            return True

        return False
        



