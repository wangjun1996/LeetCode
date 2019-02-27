# Runtime: 76 ms, faster than 57.61%    平衡二叉树
# Memory Usage: 11.5 MB, less than 97.13%
# 思路：递归法。maxDepth()方法求子树的高度，二叉树平衡的条件是每个子树都满足 abs(leftMaxDepth - rightMaxDepth) <= 1

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        leftMaxDepth = self.maxDepth(root.left)
        rightMaxDepth = self.maxDepth(root.right)
        # print(leftMaxDepth)
        # print(rightMaxDepth)

        if abs(leftMaxDepth - rightMaxDepth) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
    
    # maxDepth() 求子树的高度
    def maxDepth(self, root):
        if root == None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

if __name__ == '__main__':
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(2)
    p.right.left = TreeNode(3)
    p.right.right = TreeNode(3)
    p.left.left = TreeNode(3)
    p.left.right = TreeNode(3)
    p.left.left.left = TreeNode(4)
    p.right.right.left = TreeNode(4)
    print(Solution().isBalanced(p))