class Solution:
    def maxProfit(self, prices):
        
        if len(prices) == 2:
            if prices[-1]> prices[0]:
                return prices[-1]-prices[0]
            else:
                return 0
        profits_forward = [0]* len(prices)
        profits_backword = [0]* len(prices)
        cur_min = prices[0]
        cur_max = prices[-1]
        max_profit = 0
        for i in range(1,len(prices)-1):
            cur_min = min(prices[i],cur_min)
            if prices[i] > cur_min:
                profits_forward[i] = prices[i]- cur_min
            else:
                profits_forward[i] = profits_forward[i-1]
            
            cur_max = max(cur_max,prices[len(prices)-1-i])
            if prices[len(prices)-1-i] < cur_max:
                profits_backword[len(prices)-i] = cur_max -  prices[len(prices)-1-i]
            else:
                profits_backword[len(prices)-i] = profits_backword[len(prices)-i+1]
        
        for i in range(len(prices)-1):
            max_profit = max(max_profit,profits_backword[i]+ profits_forward[i+1])
        
        print(profits_forward,profits_backword)
        return max_profit

prices = [3,2,6,5,0,3]
#prices = [3,3,5,0,0,3,1,4]
obj = Solution()
print(obj.maxProfit(prices))