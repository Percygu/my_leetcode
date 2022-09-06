class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0,0] for _ in range(n)]
        dp[0][0] = 0                    # 第一天不持有股票，最大利润为0
        dp[0][1] = -prices[0]           # 第一天买入了股票，花费了prices[i]的钱，最大利润为
        for i in range(1,n):
            dp[i][0] = max(dp[i-1],dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1],-prices[i])
        return dp[-1][0]

