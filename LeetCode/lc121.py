# Runtime: 44 ms, faster than 82.32%    买卖股票的最佳时机
# Memory Usage: 12.9 MB, less than 68.57%
# 思路：动态规划。前i天的最大收益 = max{前i-1天的最大收益，第i天的价格-前i-1天中的最小价格}

class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        min_p, max_p = 999999, 0
        for i in range(len(prices)):
            min_p = min(min_p, prices[i])
            max_p = max(max_p, prices[i] - min_p)
        return max_p

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    prices2 = [1,2,3,4,5]
    print(Solution().maxProfit(prices))        