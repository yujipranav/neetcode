class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # two pointers
        n = len(prices)
        res = 0
        l, r = 0, 1
        
        while r < n:
            if prices[l] < prices[r]:
                maxx = prices[r] - prices[l]
                res = max(res, maxx)
            else:
                l = r

            r+=1

        return res

 # brute force
        # n = len(prices)
        # res = 0

        # for i in range(n):
        #     for j in range(i+1,n):
        #         maxx = prices[j] - prices[i]
        #         res = max(res, maxx)

        # return res
            
    

            
