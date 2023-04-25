class Solution:
    def maxProfit(self, prices):
        plen = len(prices)
        profit = [0] * plen
        fw_min = prices[0]
        fw_profit = 0
        bc_max = prices[-1]
        bc_profit = 0
        
        for i in range(plen):
            fw_min = min(prices[i],fw_min)
            fw_profit = max(fw_profit,prices[i]-fw_min)
            profit[i] += fw_profit
            bc_max = max(prices[plen-1-i],bc_max)
            if i> 0: bc_profit = max(bc_profit,bc_max-prices[plen-i-1])
            profit[plen-i-1] += bc_profit
                     
        print(profit)       
        return max(profit)
        

prices = [6,1,3,2,4,7]
#prices = [3,3,5,0,0,3,1,4]
obj = Solution()
print(obj.maxProfit(prices))