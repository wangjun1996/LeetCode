# Runtime: 48 ms, faster than 95.59%    二叉树的最小深度
# Memory Usage: 9.4 MB, less than 22.45%
# 思路：递归法

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            if root.left and root.right:
                return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
            elif root.left:
                return 1 + self.minDepth(root.left)
            elif root.right:
                return 1 + self.minDepth(root.right)
            else:
                return 1
        else:
            return 0

if __name__ == '__main__':
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    p.right.left = TreeNode(4)
    p.right.right = TreeNode(5)
    print(Solution().minDepth(p))