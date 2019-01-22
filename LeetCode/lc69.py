# 2556ms    x的平方根
# 思路：从 1 开始循环，若 i 的平方大于 x，则返回 i-1

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        for i in range(1, x+2):
            if i*i > x:
                return i - 1

if __name__ == '__main__':
    x = 9
    print(Solution().mySqrt(x))