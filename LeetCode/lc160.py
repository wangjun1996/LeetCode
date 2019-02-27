# Runtime: 204 ms, faster than 76.32%   相交链表
# Memory Usage: 40.9 MB, less than 74.30%
# 思路：把两个单链表看作是两段线段，以两条线段相加的和不变这个条件，分别遍历两个链表。
# 定义两个指针, 第一轮让两个到达末尾的节点指向另一个链表的头部, 最后如果相遇则为交点(在第一轮移动中恰好抹除了长度差)
# 两个指针等于移动了相同的距离, 有交点就返回, 无交点就是各走了两条指针的长度
# https://blog.csdn.net/qq_34364995/article/details/80518198#commentBox

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        pA = headA
        pB = headB
        # 在这里第一轮体现在pA和pB第一次到达尾部会移向另一链表的表头, 而第二轮体现在如果pA或pB相交就返回交点, 不相交最后就是null==null
        while pA != pB:
            if pA == None:
                pA = headB
            else:
                pA = pA.next
            if pB == None:
                pB = headA
            else:
                pB = pB.next
        return pA

if __name__ == '__main__':
    a = [0,9,1,2,4]
    b = [3,2,4]
    headA = ListNode(0)
    currentA = headA
    for i in range(len(a)):
        currentA.next = ListNode(a[i])
        currentA = currentA.next

    headB = ListNode(0)
    currentB = headB
    for i in range(len(b)):
        currentB.next = ListNode(b[i])
        currentB = currentB.next
    print(Solution().getIntersectionNode(headA.next, headB.next))
    