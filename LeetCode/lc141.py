# Runtime: 40 ms, faster than 100.00%   环形链表
# Memory Usage: 17.1 MB, less than 36.17%
# 思路：使用快慢指针，若指针相遇则判断有环。
# 让快慢指针都从链表头开始遍历，快指针每次向前移动两个位置，慢指针每次向前移动一个位置；如果快指针到达NULL，说明链表以NULL为结尾，没有环。如果快指针追上慢指针，则表示有环。

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        fast = head
        slow = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
