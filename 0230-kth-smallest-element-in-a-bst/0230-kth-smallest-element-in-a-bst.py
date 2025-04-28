# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        
        def inorder(node):
            nonlocal k
            if not node:
                return None
            
            left = inorder(node.left)
            if left is not None:
                return left
            
            k -= 1

            if k == 0:
                return node
            
            return inorder(node.right)
        
        ans = inorder(root)
        return ans.val if ans else 0
        #return ans[k-1]
            
        