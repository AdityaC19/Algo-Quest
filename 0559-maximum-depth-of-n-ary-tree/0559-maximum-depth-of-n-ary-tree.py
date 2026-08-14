"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        max_sum = 0
        def dfs(node):
            nonlocal max_sum
            maxDepth = 0
            if not node:
                return 0
            
            for child in node.children:
                depth = max(dfs(child), 0)
                cur_sum = maxDepth + depth + node.val
                max_sum = max(max_sum, cur_sum)
                maxDepth = max(maxDepth, depth)
            
            return node.val + maxDepth
        
        dfs(root)
        return max_sum

        