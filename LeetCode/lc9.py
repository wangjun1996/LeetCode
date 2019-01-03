# Runtime: 256  ms, faster than 96.74%  回文数

class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        str1 = str(x)[::-1]
        return True if str1 == str(x) else False

if __name__ == '__main__':
    x = 123
    print(Solution().isPalindrome(x))