# Runtime: 60 ms, faster than 18.26%    搜索插入位置
# 思路：比较每个 nums[i]值与 target 值，若相等则返回当前位置 i，若 nums[i] > target 说明该 List 没有target值，返回 i,注意特殊情况

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == target or nums[i] > target:
                return i
        return i+1
        

if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 5
    print(Solution().searchInsert(nums, target))