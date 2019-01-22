# Runtime: 56 ms, faster than 54.14%    爬楼梯
# 思路：《递归+数组》  参考 https://blog.csdn.net/qq_38595487/article/details/79686081
# n个台阶，一开始可以爬 1 步，也可以爬 2 步，那么n个台阶爬楼的爬楼方法就等于 一开始爬1步的方法数 + 一开始爬2步的方法数，
# 这样我们就只需要计算n-1个台阶的方法数和n-2个台阶方法数，同理，计算n-1个台阶的方法数只需要计算一下n-2个台阶和n-3个台阶，
# 计算n-2个台阶需要计算一下n-3个台阶和n-4个台阶…… 而我们可以很容易知道，1个台阶只有 1 种方法，2个台阶有 2 种方法。
# 建立一个数组nums[n+1]来保存n个台阶的爬楼方法数，这样可以避免重复计算。直到n-1<=2,n-2<=2时，可以直接求得n的个数，返回上一层递归。

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n ==2:
            return 2
        nums = [0,1,2]
        for i in range(3,n):
            nums.insert(i, 0)
        Solution().climb(nums, n)
        return nums[n]
    
    def climb(self, nums, n):
        x = n-1
        y = n-2
        if x > 2 and nums[x] == 0:
            Solution().climb(nums, x)
        if y > 2 and nums[y] == 0:
            Solution().climb(nums, y)
        nums.insert(n, nums[x]+nums[y])

if __name__ == '__main__':
    n = 10
    print(Solution().climbStairs(n))