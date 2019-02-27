# Runtime: 32 ms, faster than 100.00%   只出现一次的数字
# Memory Usage: 14.2 MB, less than 36.64%
# 思路：异或，相同为0，不同为1. 异或同一个数两次，原数不变。

class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'int':
        a = 0
        for num in nums:
            a = a ^ num
        return a

if __name__ == '__main__':
    list = [2,2,1]
    list2 = [4,1,2,1,2]
    print(Solution().singleNumber(list2))  