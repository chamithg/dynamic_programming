class Solution:
    def maxProfit(self, prices):
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
                profits_backword[len(prices)-1-i] = cur_max -  prices[len(prices)-1-i]
            else:
                profits_backword[len(prices)-1-i] = profits_backword[len(prices)-i]

            max_profit = max (profits_forward[i]+profits_backword[i],profits_forward[len(prices)-i]+profits_backword[len(prices)-i])
        print(profits_backword,profits_forward)
        return max_profit

prices = [1,2,3,4,5]
#prices = [3,3,5,0,0,3,1,4]
obj = Solution()
print(obj.maxProfit(prices))