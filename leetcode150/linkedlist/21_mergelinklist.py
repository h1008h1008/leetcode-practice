# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur1 = list1
        cur2 = list2
        head = ListNode(0)
        cur = head
        while cur1 and cur2:
            if (cur1.val > cur2.val):
                cur.next = ListNode(cur2.val)
                cur = cur.next
                cur2 = cur2.next
            else:
                cur.next = ListNode(cur1.val)
                cur = cur.next
                cur1 = cur1.next
        if cur1:
            cur.next = cur1
        else:
            cur.next = cur2
        return head.next
