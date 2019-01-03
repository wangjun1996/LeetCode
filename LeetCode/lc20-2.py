# Runtime: 56 ms, faster than 19.76%    多种括号匹配
# 思路：将字符串中成对的括号替换成空，若最后字符串为空即成功匹配，反之失败

class Solution:
    def isValid(self, s):
        n = len(s)
        if n == 0:
            return True
        elif n % 2 == 1:
            return False
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()', '').replace('[]', '').replace('{}', '')
        return True if s == '' else False   

if __name__ == '__main__':
    s = '()[]{}'
    print(Solution().isValid(s))
