# Runtime: 56 ms, faster than 24.71%    最长公共前缀
# 思路：先比较第1个字符串和第2个字符串，找到他们的最长公共前缀，然后将结果与第3个字符串比较，递归执行即可

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        elif len (strs) == 1:
            return strs[0]
        else:
            for i in range(len(strs)-1):
                temp = strs[i]
                if temp == "":
                    return "" 
                if i == 0:
                    res = self.firstmatch(temp, strs[i+1])
                else:
                    res = self.firstmatch(res, strs[i+1])
                if res == "":
                    return ""
            return res

    def firstmatch(self,a,b):   # 比较两个数组中从头开始相同的字符串
        result = ""
        for i in range(len(a)):
            if (len(a) > len(b) and i >= len(b)) or a[i] != b[i]:
                break
            if (len(a) < len(b) and i >= len(a)) or a[i] != b[i]:
                break
            result +=a[i]
        return result               

if __name__ == '__main__':
    s = ["flower","flow","flight"]
    a = ["flower","flower","flower"]
    b = ["dog","racecar","car"]
    c = ["aaa"]          # len(strs) = 1
    d = ["aa","a"]       # len(strs) = 2
    e = ["","","aaa"]    # len(strs) = 3
    f = ["baab","bacb","b","cbc"]
    g = ["caa","","a","acb"]
    h = ["b","cb","cab"]
    i = ["acc","aaa","aaba"]
    print(Solution().longestCommonPrefix(i))