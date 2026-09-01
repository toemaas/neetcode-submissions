# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        for i in range(n):
            curr = curr.next
        
        

        node = dummy = ListNode(0, head)
        while curr:
            node = node.next
            curr = curr.next
        
        node.next = node.next.next

        return dummy.next