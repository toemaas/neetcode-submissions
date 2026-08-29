# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        exmaple:
        981 + 99999
        1 8 9
        9 9 9 9 9
        0 8 9 0 0 1
        Idea: two pointer two pass
        iterate through keeping track of ones place by % 10
        increment both pointers once, keep going until end of one list
        iterate through the remaining list
        if there's remainder, create a new node and add it
        return the new list
        '''
        new = ListNode(0)
        first, second = l1, l2
        remainder = 0
        head = new
        while first and second:
            sum = first.val + second.val + new.val
            new.val = sum % 10
            remainder = sum // 10
            if remainder > 0:
                new.next = ListNode(remainder)
            else:
                new.next = ListNode(0)
            first = first.next
            second = second.next
            if not first and not second:
                new.next = None
            else:
                new = new.next
        
        while first:
            sum = first.val + new.val
            new.val = sum % 10
            remainder = sum // 10
            if remainder > 0:
                new.next = ListNode(remainder)
            else:
                new.next = ListNode(0)
            first = first.next
            if not first:
                new.next = None
            else:
                new = new.next

        while second:
            sum = second.val + new.val
            new.val = sum % 10
            remainder = sum // 10
            if remainder > 0:
                new.next = ListNode(remainder)
            else:
                new.next = ListNode(0)
            second = second.next
            if not second:
                new.next = None
            else:
                new = new.next
        
        if remainder != 0:
            new.next = ListNode(remainder)
        return head