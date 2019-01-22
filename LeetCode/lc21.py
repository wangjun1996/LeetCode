# Runtime: 44 ms, faster than 99.41%    合并两个有序链表
# 思路：新建一个链表，然后比较两个链表中的元素值，把较小的那个链到新链表中，由于两个输入链表的长度可能不同，所以最终会有一个链表先完成插入所有元素，则将另一个未完成的链表直接链入新链表的末尾

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        current = head
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        if l1 == None:
            current.next = l2
        if l2 == None:
            current.next = l1
        return head.next

if __name__ == '__main__':
    a = [1,2,4]
    b = [1,3,4]
    head1 = ListNode(0)
    head2 = ListNode(0)
    current1 = head1
    current2 = head2
    for i in range(len(a)):
        current1.next = ListNode(a[i])
        current1 = current1.next
        # print(current1.val)

    for i in range(len(b)):
        current2.next = ListNode(b[i])
        current2 = current2.next
        # print(current2.val)
    
    result = Solution().mergeTwoLists(head1.next,head2.next)
    for i in range(6):
        print(result.val)
        result =result.next