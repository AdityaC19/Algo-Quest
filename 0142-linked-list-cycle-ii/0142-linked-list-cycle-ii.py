# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = set()
        curr = head

        while curr:
            if curr in s:
                return curr
            else:
                s.add(curr)
                curr = curr.next
        # fast = slow = head

        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next
        #     if slow == fast:
        #         slow = head
        #         while slow != fast:
        #             slow = slow.next
        #             fast = fast.next
        #         return slow
                        
        
        return None
        