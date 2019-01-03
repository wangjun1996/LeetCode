# Runtime: 52 ms, faster than 99.24%

class Solution:
    def reverse(self, x):
        sup = 2**31 - 1
        inf = -2**31

        if x >= 0:
            y = int(str(x)[::-1])   # str[::-1]翻转字符串
            return y if y <= sup else 0
        else:
            y = int('-' + str(x)[:0:-1])
            return y if y >= inf else 0


if __name__ == '__main__':
    x = -423235
    print(Solution().reverse(x))