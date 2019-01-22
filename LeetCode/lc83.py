# 76 ms, faster than 81.09%     删除排序链表中的重复元素
# 思路：原链表不变，新建一个链表，遍历原链表，将原链表第一个结点值赋值为flag，若当前结点的值不等于flag，则将该结点插入新链表，若等于则原链表往下继续遍历
# head：原链表的头结点   h：新链表的头结点   current：遍历新链表的结点    flag：原链表当前结点的值

# 定义单链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        h = ListNode(head.val)
        current = h
        flag = head.val
        while head != None:
            if flag == head.val:
                head = head.next
            else:
                current.next = ListNode(head.val)
                current = current.next
                flag = head.val
                head = head.next
        return h

if __name__ == '__main__':
    a = [1,1,2,3,3,3,3,4,4,5,6,6]
    head = ListNode(0)
    current = head
    for i in range(len(a)):
        current.next = ListNode(a[i])
        current = current.next
    
    result = Solution().deleteDuplicates(head.next)
    while result != None:
        print(result.val)
        result = result.next