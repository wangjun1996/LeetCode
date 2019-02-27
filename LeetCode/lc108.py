# Runtime: 64 ms, faster than 67.30%    将有序数组转换为二叉搜索树
# 思路：所谓二叉搜索树，是一种始终满足 左<根<右 的特性的二叉树。采用二分法来创建平衡二叉树，根结点刚好为数组中间的节点，根节点的左子树的根是数组左边部分的中间节点，根节点的右子树是数据右边部分的中间节点；

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == None or len(nums) == 0:
            return None
        return self.recursion(nums, 0, len(nums)-1)
    
    def recursion(self, nums, left, right):
        if left <= right:
            mid = int((left + right)/2)
            p = TreeNode(nums[mid])
            p.left = self.recursion(nums, left, mid-1)
            p.right = self.recursion(nums, mid+1, right)
            return p
        else:
            return None

if __name__ == '__main__':
    nums = [-10,-3,0,5,9]
    print(Solution().sortedArrayToBST(nums).val)