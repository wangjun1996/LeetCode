# Runtime: 40 ms, faster than 99.05%    买卖股票的最佳时机 II
# Memory Usage: 13 MB, less than 29.11%
# 思路：贪心算法。只要后一天比前一天股价高就卖
# 贪心算法是指，在对问题求解时，总是做出在当前看来是最好的选择。也就是说，不从整体最优上加以考虑，他所做出的是在某种意义上的局部最优解。

class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        profitSum = 0
        for day in range(len(prices)-1):
            profit = prices[day+1] - prices[day]
            if profit > 0:
                profitSum += profit
        return profitSum

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    prices2 = [1,2,3,4,5]
    prices3 = [7,6,4,3,1]
    prices4 = [6,1,3,2,4,7]
    print(Solution().maxProfit(prices))        