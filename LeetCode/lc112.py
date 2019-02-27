# Runtime: 48 ms, faster than 99.96%    路径总和
# Memory Usage: 8.7 MB, less than 42.38%
# 思路：递归法

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: 'TreeNode', sum: 'int') -> 'bool':
        if root == None:
            return False
        if root.left == None and root.right == None:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

if __name__ == '__main__':
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    p.right.left = TreeNode(4)
    p.right.right = TreeNode(5)
    print(Solution().hasPathSum(p, 7))