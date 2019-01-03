# Runtime: 60 ms, faster than 26.61%    实现strStr()。即从 haystack 中查找 needle 第一次出现的位置
# 思路：暴力破解法，使用Python切片，从 i=0 开始匹配 len(needle) 个字符串，匹配 len(haystack) - len(needle)+1 次
# 注：可用 KMP 算法实现，效率更高，但比较难理解

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle)+1):
            # print(haystack[i:i+len(needle)])
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
                    

if __name__ == '__main__':
    haystack = "hello"
    needle = "lol"
    # haystack = "aaaaa"
    # needle = "bba"
    # haystack = "mississippi"
    # needle = "issip"
    print(Solution().strStr(haystack, needle))