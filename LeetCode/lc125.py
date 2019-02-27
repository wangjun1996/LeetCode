# Runtime: 60 ms, faster than 82.35%    验证回文串
# Memory Usage: 12.5 MB, less than 96.86%
# 思路：先将字符串转换成小写，再去除字母和数字以外的字符，最后比较逆序后的字符串与原字符串是否一样
# 方法二：正则表达式。s = re.sub('[^A-Za-z0-9]', '', s).lower()     return s == s[::-1]

class Solution:
    def isPalindrome(self, s: 'str') -> 'bool':
        lowerStr = s.lower()    # 将字符串转换成小写
        resStr = ""
        for i in range(len(lowerStr)):
            if lowerStr[i].isalpha() or lowerStr[i].isdigit():  # 将 lowerStr 中的字母和数字添加到 resStr
                resStr += lowerStr[i]
        return resStr[::-1] == resStr

if __name__ == '__main__':
    str = "A man, a plan, a canal: Panama"
    str2 = "race a car"
    print(Solution().isPalindrome(str))  