# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        
        def inorder(node):
            if not node:
                return 
            
            left = inorder(node.left)
            ans.append(node.val)
            right = inorder(node.right)
        
        inorder(root)
        return ans[k-1]
            
        