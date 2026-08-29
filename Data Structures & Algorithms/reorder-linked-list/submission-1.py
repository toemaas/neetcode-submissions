# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        prev = slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        curr = head
        cur2 = prev
        while cur2:
            nxt = curr.next
            nxt2 = cur2.next
            curr.next = cur2
            cur2.next = nxt
            curr = nxt
            cur2 = nxt2