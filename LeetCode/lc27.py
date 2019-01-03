# Runtime: 56 ms, faster than 24.43%    移除元素
# 思路：从 nums 的第1个位置开始与 val 比较，若相等则删除，否则i+1

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
        return len(nums)

if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(Solution().removeElement(nums, val))