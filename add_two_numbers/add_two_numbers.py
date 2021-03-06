#leetcode 2
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        carry = 0
        dummyHead = ListNode(0)
        dummyTail = dummyHead
        while p1 != None and p2 != None:
            dummyTail.next = ListNode( (p1.val + p2.val + carry) % 10 )
            dummyTail = dummyTail.next 
            carry = ( p1.val + p2.val + carry ) / 10
            p1 = p1.next
            p2 = p2.next
        
        if p1 is None and p2 is None:
            if carry != 0:
                dummyTail.next = ListNode(carry)
                dummyTail = dummyTail.next
            return dummyHead.next
        else:
            if p1 != None:
                p = p1
            else:
                p = p2
            while p != None:
                dummyTail.next = ListNode( (p.val + carry) % 10 )
                dummyTail = dummyTail.next
                carry = ( p.val + carry ) / 10
                p = p.next
            if carry != 0:
                dummyTail.next = ListNode(carry)
                dummyTail = dummyTail.next
            return dummyHead.next
            
            
#cleaner solution
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummyHead = dummyTail = ListNode(0)
        while l1 or l2 or carry:
            v1 = 0
            v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            dummyTail.next = ListNode( (v1 + v2 + carry) % 10 )
            dummyTail = dummyTail.next
            carry = (v1 + v2 + carry) / 10
        
        return dummyHead.next
