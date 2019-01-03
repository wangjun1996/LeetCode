# Runtime: 60 ms, faster than %    移除元素
# 思路：从 nums的第1个位置开始与 val 比较，若相等则用该值覆盖nums[j]，否则 i+1 继续运行

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] != val:
                nums[j] = nums[i]
                i += 1
                j += 1
            else:
                i += 1
        return j

if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(Solution().removeElement(nums, val))