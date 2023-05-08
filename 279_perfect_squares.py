class Solution:
    def numSquares(self, n):
        
        #  similar to coin change problem
    
        
        squares = []
        i = 1
        while i*i <= n:
            squares.append(i*i)
            i+=1
                
        dp = [9999] * (n+1)
        
        for i in range(1,n+1):
            for s in squares:
                if s <= i:
                    if i % s == 0:
                        dp[i] = min(dp[i],i//s)
                    else:
                        dp[i] = min(dp[i],dp[i-s]+1)
        return dp[n]
                
            
        
n = 12
obj = Solution()
print(obj.numSquares(n))