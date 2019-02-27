# Runtime: 32 ms, faster than 100.00%   杨辉三角
# Memory Usage: 12.2 MB, less than 100.00%
# 思路：
# 当 numRows=0,1,2 三种特殊情况时，返回固定结果。
# 当 numRows>2 时，循环调用 addToList()，将生成的 子List (即代码中的 r[ ]) 插入到 母List (即代码中的 res[ ]) 中


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]

        res = [[1],[1,1]]
        i = 3
        while i <= numRows:
            self.addToList(res, i)
            i += 1
        return res
    
    def addToList(self, res, numRows):
        r = []
        for i in range(numRows):
            if i == 0 or i == numRows-1:
                r.append(1)
            else:
                r.append(res[-1][i-1]+res[-1][i])
        res.append(r)

if __name__ == '__main__':
    numRows = 5
    print(Solution().generate(numRows))