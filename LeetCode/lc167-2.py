# Runtime: 20 ms, faster than 100.00%   两数之和 II - 输入有序数组
# Memory Usage: 10.9 MB, less than 45.95%
# 思路：使用两个指针，分别指向list的头和尾


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1

if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 17
    print(Solution().twoSum(numbers, target))
