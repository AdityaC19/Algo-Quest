# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        
        def helper(root, p, q):
            if not root:
                return

            if p == root or q == root:
                return root
            
            left = helper(root.left, p, q)
            right = helper(root.right, p, q)
            
            if left and right:
                return root
            
            return left or right
        
        return helper(root, p, q)


        
        
        # def helper1(root, p, q):
        #     if not root:
        #         return None
        #     if root == p or root == q:
        #         return root

        #     left = helper1(root.left, p, q)
        #     #right = helper(root.right, p, q)
        #     ancestor.add(root)

        #     if left and right:
        #         return root




