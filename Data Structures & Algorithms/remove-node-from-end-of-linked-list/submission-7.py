# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        remove = head
        for i in range(n + 1):
            if not remove:
                return head.next
            remove = remove.next
        curr = head

        while remove:
            curr = curr.next
            remove = remove.next

        curr.next = curr.next.next

        return head