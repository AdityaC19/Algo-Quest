"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        hmap = {}

        if not head: return None

        while curr:
            node = Node(curr.val)
            hmap[curr] = node
            curr = curr.next
        
        curr = head

        while curr:
            new_node = hmap[curr]
            if curr.next:
                new_node.next = hmap[curr.next]
            else:
                None
            if curr.random:
                new_node.random = hmap[curr.random]
            else:
                None
            curr = curr.next
        
        return hmap[head]
        