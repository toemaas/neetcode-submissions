# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return

        while len(lists) > 1:
            m = []
            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    m.append(self.mergeTwoLists(lists[i], lists[i + 1]))
                else:
                    m.append(lists[i])

            lists = m
        
        return lists[0]

    def mergeTwoLists(self, p, q):
        dummy = curr = ListNode()

        while p and q:
            if p.val < q.val:
                curr.next = p
                p = p.next
            else:
                curr.next = q
                q = q.next
            curr = curr.next
        
        curr.next = p or q

        return dummy.next