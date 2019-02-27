# Runtime: 92 ms, faster than 12.94%    只出现一次的数字
# Memory Usage: 13.5 MB, less than 98.70%
# 思路：先排序，然后比较相邻元素，若相等则删除两个元素，最后剩的一个元素即结果
# 注：sort 排序算法时间复杂度 O(n log n) 不是线性的。

class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'int':
        nums.sort()
        i= 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                del(nums[i])
                del(nums[i])
                i = 0
            else:
                i += 1
        return nums[0]

if __name__ == '__main__':
    list = [2,2,1]
    list2 = [4,1,2,1,2]
    print(Solution().singleNumber(list))  