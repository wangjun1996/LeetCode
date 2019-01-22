# Runtime: 48 ms, faster than 99.27%    爬楼梯
# 思路：《斐波那契数列》    1 2 3 5 8 13 21 ... 

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = b = 1
        for i in range(n):
            a, b = b, a + b
        return a

if __name__ == '__main__':
    n = 3
    print(Solution().climbStairs(n))