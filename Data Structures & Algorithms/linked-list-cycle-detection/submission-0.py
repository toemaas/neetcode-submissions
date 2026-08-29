# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cycle1 = head
        cycle2 = head.next
        while cycle1 and cycle2:
            if cycle1 == cycle2:
                return True
            cycle1 = cycle1.next
            cycle2 = cycle2.next
            if cycle2:
                cycle2 = cycle2.next
        return False