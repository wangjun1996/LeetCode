# Runtime: 20 ms, faster than 100.00%   两数之和 II - 输入有序数组
# Memory Usage: 11 MB, less than 29.73%
# 思路：使用字典

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        # enumerate(list) 同时列出数据和数据下标
        for i,num in enumerate(numbers):
            if target - num in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i
 
        
if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 22
    print(Solution().twoSum(numbers, target))