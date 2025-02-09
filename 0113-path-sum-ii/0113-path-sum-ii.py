# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        sol = []
        
        def root_to_leaf_path(root, curSum):
            if not root:
                return []
            
            curSum += root.val
            ans.append(root.val)

            if not root.left and not root.right and curSum == targetSum:
                sol.append(ans.copy())
            else:
                root_to_leaf_path(root.left, curSum)
                root_to_leaf_path(root.right, curSum)
            ans.pop()
        
        root_to_leaf_path(root, 0)
        return sol