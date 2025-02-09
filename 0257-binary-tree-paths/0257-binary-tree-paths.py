# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, node: Optional[TreeNode]) -> List[str]:
        temp = []
        res = []

        def dfs(node):
            if not node:
                return 
            
            temp.append(node.val)

            if not node.left and not node.right:
                res.append("->".join(map(str, temp)))

            else:
                dfs(node.left)
                dfs(node.right)
            temp.pop()
        
        dfs(node)
        return res
                
        