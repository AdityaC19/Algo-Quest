# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None
        isBST = [True]
        def dfs(node):
            nonlocal prev
            if not node:
                return 
            
            dfs(node.left)
            if prev is not None:
                if node.val <= prev:
                    isBST[0] = False
            prev = node.val
            dfs(node.right)
        
        dfs(root)
        return isBST[0]


        # def dfs(root):
        #     if not root:
        #         return None

        #     while root:
        #         if root.left and dfs(root.left.val) >= root.val:
        #             return False
        #         elif root.right and dfs(root.right.val) <= root.val:
        #             return False
        #         else:
        #             return True
        
        # dfs(root)