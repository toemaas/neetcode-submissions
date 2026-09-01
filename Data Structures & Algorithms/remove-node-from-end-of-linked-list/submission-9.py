# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        
        length -= n
        curr = dummy = ListNode(0, head)

        for i in range(length):
            curr = curr.next
        
        curr.next = curr.next.next

        return dummy.next