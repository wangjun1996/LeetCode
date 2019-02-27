# Runtime: 32 ms, faster than 100.00%   杨辉三角 II
# Memory Usage: 12.4 MB, less than 100.00%
# 思路：
# 当 rowIndex=0,1 两种特殊情况时，返回固定结果。
# 当 rowIndex>1 时，循环调用 addToList()，将生成的 子List (即代码中的 r[ ]) 插入到 母List (即代码中的 res[ ]) 中
# 返回 母List (即代码中的 res[ ]) 中的最后一个子List (即代码中的 r[ ]) 

class Solution:
    def getRow(self, rowIndex: 'int') -> 'List[int]':
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]

        res = [[1],[1,1]]
        i = 2
        while i <= rowIndex+1:
            self.addToList(res, i)
            i += 1
        return res[-1]
    
    def addToList(self, res, numRows):
        r = []
        for i in range(numRows):
            if i == 0 or i == numRows-1:
                r.append(1)
            else:
                r.append(res[-1][i-1]+res[-1][i])
        res.append(r)

if __name__ == '__main__':
    for i in range(33):
        print(Solution().getRow(i), "\n")