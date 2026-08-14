# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        que = deque([root])

        if not root:
            return 

        while que:
            for _ in range(len(que)):
                node = que.popleft()
                if node.val < p.val and node.val < q.val:
                    que.append(node.right)
                elif node.val > p.val and node.val > q.val:
                    que.append(node.left)
                else:
                    return node
                #if node.left: q.append(node.left)
                #if node.right: q.append(node.right)
        
        