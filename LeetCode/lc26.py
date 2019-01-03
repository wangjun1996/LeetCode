# Runtime: 88 ms, faster than 36.13%    删除排序数组中的重复项，返回数组长度
# 思路：循环数组，若下一个元素nums[i+1]等于nums[i]，就删除nums[i+1]，注意的是循环次数需要 -1，避免索引越界。

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums)-1:
            if nums[i+1] == nums[i]:
                del nums[i+1]
            else:
                i += 1
        print(nums)
        return len(nums)
       

if __name__ == '__main__':
    s =  [1,1,1,2]
    print(Solution().removeDuplicates(s))