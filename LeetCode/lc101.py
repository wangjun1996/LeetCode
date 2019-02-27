# Runtime: 40 ms, faster than 99.86%    对称二叉树
# 思路：递归法，关键在于 return p.val == q.val and self.recursion(p.left, q.right) and self.recursion(p.right, q.left)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.recursion(root.left, root.right)
        else:
            return True

    def recursion(self, p, q):
        if p and q:
            return p.val == q.val and self.recursion(p.left, q.right) and self.recursion(p.right, q.left)
        else:
            return not p and not q

if __name__ == '__main__':
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(1)
    print(Solution().isSymmetric(p))