# 96ms 	二进制求和
# 思路：先转为十进制求和再将结果转为二进制

class Solution:    
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # 获取用户输入十进制数
        # dec = int(input("输入数字："))     
        # print("十进制数为：", dec)
        # print("转换为二进制为：", bin(dec))
        # print("转换为八进制为：", oct(dec))
        # print("转换为十六进制为：", hex(dec))
        
        num=int(a,2)+int(b,2)
        ans=bin(num)
        return ans[2:]


if __name__ == '__main__':
    a = "1010"
    b = "1011"
    print(Solution().addBinary(a, b))