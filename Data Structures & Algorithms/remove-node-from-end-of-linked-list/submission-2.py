# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        brute force:
        iterate and count to get the length of list
        then iterate through len(list) - n
        then remove
        '''
        curr = head
        count = 0
        while curr:
            curr = curr.next
            count += 1
        
        first = head
        for i in range(count - n - 1):
            first = first.next
        
        if count - n - 1 < 0:
            head = head.next
        elif first.next:
            first.next = first.next.next
        else:
            head = None
        
        return head
        
