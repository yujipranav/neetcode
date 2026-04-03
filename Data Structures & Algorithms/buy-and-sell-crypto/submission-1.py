class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # brute force
        n = len(prices)
        res = 0

        for i in range(n):
            for j in range(i+1,n):
                maxx = prices[j] - prices[i]
                res = max(res, maxx)

        return res

        
