class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        INF = 10**9

        dp = [[0, -INF] for _ in range(k+1)]

        for price in prices:
            for t in range(k, 0, -1):
                dp[t][0] = max(dp[t][0], dp[t][1] + price)
                dp[t][1] = max(dp[t][1], dp[t-1][0] - price)

        return dp[k][0]
