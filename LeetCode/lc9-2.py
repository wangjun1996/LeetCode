# Runtime: 272 ms, faster than 80.61%   回文数

class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        temp = x
        y = 0
        while(temp!=0):
            y = y*10 + temp%10
            temp//=10
        return True if x == y else False

if __name__ == '__main__':
    x = 123
    print(Solution().isPalindrome(x))