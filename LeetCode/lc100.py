# Runtime: 52 ms, faster than 23.84%    相同的树
# 思路：递归法

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        if p != None and q != None and p.val == q.val:
            return Solution().isSameTree(p.left, q.left) and Solution().isSameTree(p.right, q.right)
        else:
            return False

if __name__ == '__main__':
    p = TreeNode(1)
    p.left = TreeNode(2)
    q = TreeNode(1)
    q.right = TreeNode(2)
    print(Solution().isSameTree(p, q))