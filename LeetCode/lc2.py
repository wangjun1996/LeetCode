# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy = l = ListNode(0)
        while True:
            if not l1 and not l2:
                break
            if l1 and l2:
                val = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1 and not l2:
                val = l1.val + carry
                l1 = l1.next
            elif l2 and not l1:
                val = l2.val + carry
                l2 = l2.next
            carry = val // 10
            l.next = ListNode(val % 10)
            l = l.next

        if carry != 0:
            l.next = ListNode(carry)
            l = l.next
        return dummy.next
