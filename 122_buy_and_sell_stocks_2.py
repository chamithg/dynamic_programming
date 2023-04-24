class Solution:
    def maxProfit(self, prices):
        profit = 0
        profit = [0] * len(prices)
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit[i] = profit[i-1] + prices[i] - prices[i-1]
            else:
                profit[i] = profit[i-1]
                
            
        print(profit)
        
        return profit[-1]



prices = [7,1,5,3,6,4]
obj = Solution()
print(obj.maxProfit(prices))