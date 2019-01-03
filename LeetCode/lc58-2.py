# 52 ms, faster than 39.99% 	最后一个单词的长度
# 思路：用 s.strip() 先删除字符串首尾的空格，再将字符串逆序，然后从头开始计算单词长度直到当前位置为空

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()   # 删除字符串首尾的空格
        if len(s) == 0:
            return 0
        s = s[::-1]

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