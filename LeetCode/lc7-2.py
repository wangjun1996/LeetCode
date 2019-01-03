# Runtime: 76 ms, faster than 37.84%

class Solution:
    def reverse(self, x):
        MAX = 2**31 - 1
        MIN = -2**31
        flag = 0
        if x < 0:
            x = -x
            flag = 1
        y = 0
        while(x!=0):
            y = y*10 + x % 10
            x = x//10
        if y > MAX or y < MIN:
            y = 0
        if flag == 1:
            return -y
        return y

if __name__ == '__main__':
    x = 123
    print(Solution().reverse(x))