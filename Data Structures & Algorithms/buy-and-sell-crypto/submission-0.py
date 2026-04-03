class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        res = 0

        for i in range(n):
            for j in range(i+1, n):
                profit = prices[j] - prices[i]
                res = max(res, profit)

        return res