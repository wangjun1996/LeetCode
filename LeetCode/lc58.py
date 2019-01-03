# 52 ms, faster than 39.99% 	最后一个单词的长度
# 思路：先将字符串逆序，然后计算从首字母开始的空格数，然后去除空格，再从头开始计算单词长度直到当前位置为空

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        s = s[::-1]

        # 计算从首字母开始的空格数，然后去除空格
        blank = 0
        for k in range(len(s)):
            if s[k] == ' ':
                blank += 1
            else:
                break
        if blank == len(s):
            return 0
        s = s[blank:]

        j = 0
        for i in range(len(s)):
            if s[i] == ' ':
                return j
            if i == len(s) - 1:
                return j + 1
            j += 1


if __name__ == '__main__':
    str = "Hello World"
    print(Solution().lengthOfLastWord(str))