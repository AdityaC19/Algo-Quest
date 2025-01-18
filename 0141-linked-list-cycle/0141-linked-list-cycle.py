# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        temp = 'a'

        while curr:
            if curr.val == temp:
                return True
            curr.val = temp
            curr = curr.next

        return False