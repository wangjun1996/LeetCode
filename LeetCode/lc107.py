# Runtime: 40 ms, faster than 99.50%    二叉树的层次遍历 II（自底向上的层次遍历）
# 思路：递归法。注意 res[-1]：倒数第一个数组, res[-2]：倒数第二个数组...

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.recursion(root, 0, res)
        return res

    def recursion(self, p, level, res):
        if p:
            if len(res) < level + 1:
                res.insert(0, [])
            # print(p.val)
            res[-(level+1)].append(p.val)
            self.recursion(p.left, level+1, res)
            self.recursion(p.right, level+1, res)

if __name__ == '__main__':
    p = TreeNode(3)
    p.left = TreeNode(9)
    p.right = TreeNode(20)
    p.right.left = TreeNode(15)
    p.right.right = TreeNode(7)
    print(Solution().levelOrderBottom(p))