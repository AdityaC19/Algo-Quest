# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return
            
            if node == p or node == q:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            # cond?
            if left is not None and right is not None:
                return node
            
            return left if left is not None else right

        return dfs(root)     
        

        # node = root

        # while node:
        #     if node.val < p.val and node.val < q.val:
        #         node = node.right
        #     elif node.val > p.val and node.val > q.val:
        #         node = node.left
        #     else:
        #         return node


        