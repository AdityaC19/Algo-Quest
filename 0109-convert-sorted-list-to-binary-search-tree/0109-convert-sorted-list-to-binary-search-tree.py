# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mapListToValues(self, head):
        values = []
        while head is not None:
            values.append(head.val)
            head = head.next
        return values

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        arr = self.mapListToValues(head)

        def dfs(left, right):
            if left > right:
                return None

            mid = left + (right - left) // 2
            root = TreeNode(arr[mid])
            root.left = dfs(left, mid-1)
            root.right = dfs(mid+1, right)

            return root
        
        return dfs(0, len(arr)-1)

