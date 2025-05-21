# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []
        def inorder(node):
            if not node:
                return None
            
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)

        inorder(root)

        if sorted(ans) == ans and len(set(ans)) == len(ans):
            return True

        return False        