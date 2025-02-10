# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        q = deque([root])
        min_length = float('inf')
        level = 0

        if not root:
            return 0

        while q:
            q_len = len(q)

            for _ in range(q_len):
                node = q.popleft()
                if not node.left and not node.right:
                    min_length = min(min_length, level)
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
            level += 1
        
        return min_length+1

                    


        # def dfs(node):
        #     if not node:
        #         return 0

        #     left_tree = dfs(node.left)
        #     right_tree = dfs(node.right)
            
        #     if not node.left or not node.right:
        #         return 1 + max(left_tree, right_tree)            

        # return dfs(root)
        