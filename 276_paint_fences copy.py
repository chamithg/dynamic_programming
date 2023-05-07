class Solution:
    def numWays(self,n,k):
        if n == 0 :
            return 0
        dp = [0] * (n+1)

        for i in range(n+1):
            if i == 0:
                dp[i] = 0
            elif i == 1:
                dp[i] = k
            elif i == 2:
                dp[i] = k * k
            else:
                dp[i] =( dp[i-1] + dp[i-2]) * (k-1)

        return dp[n]
n = 3
k = 4
obj = Solution()
print(obj.numWays(n,k))