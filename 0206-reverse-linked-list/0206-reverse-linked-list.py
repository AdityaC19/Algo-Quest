# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        curr = head

        while curr:
            res.append(curr.val)
            curr = curr.next
        
        rev_res = res[::-1]

        curr = head
        
        for i in rev_res:
            curr.val = i
            curr = curr.next
        
        return head


        
