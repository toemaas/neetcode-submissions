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
        slow.next = prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # 2, 4
        # 8, 6
        # prev = head of reversed list
        curr = head

        while prev:
            t1 = curr.next
            t2 = prev.next
            curr.next = prev
            prev.next = t1
            curr = t1
            prev = t2
