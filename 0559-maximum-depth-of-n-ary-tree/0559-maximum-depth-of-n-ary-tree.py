"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(node):
            maxDepth = 0
            if not node:
                return 0
            
            for child in node.children:
                depth = dfs(child)
                maxDepth = max(maxDepth, depth)
            
            return 1 + maxDepth
        
        return dfs(root)
        