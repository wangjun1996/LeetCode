# Runtime: 56 ms, faster than 24.71%    最长公共前缀

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        if len(strs) == 0:
            return ""
        else:
            for each in zip(*strs): # zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象
                if len(set(each)) == 1: # set() 创建一个无序不重复元素集
                    res += each[0]
                else:
                    return res
        return res
        
if __name__ == '__main__':
    s = ["flower","flow","flight"]
    a = ["flower","flower","flower"]
    b = ["dog","racecar","car"]
    c = ["","","aaa"]   # len(strs) = 3
    d = ["aaa"]         # len(strs) = 1
    print(Solution().longestCommonPrefix(s))