# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur = ListNode(0)
        dummy = cur
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum_val = x + y + carry
            
            carry = sum_val // 10
            cur.next = ListNode(sum_val % 10)
            cur = cur.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        if carry > 0:
            cur.next = ListNode(carry)
        
        return dummy.next
            

