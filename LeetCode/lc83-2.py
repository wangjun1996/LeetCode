# 92 ms, faster than 22.22%     删除排序链表中的重复元素
# 思路：在原链表上修改。判断头元素与头元素下一节点的值是否相等，若相等则cur.next = cur.next.next，若不等则继续向下遍历

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
        if head is None:
            return head
        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

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