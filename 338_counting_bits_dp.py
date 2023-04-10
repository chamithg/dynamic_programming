class Solution:
    def countBits(self, n):    
    # Let f(i) := i's # Of 1's in bitmask
    # f(i) = f(i / 2) + i % 2
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i // 2] + (i & 1)
        return ans
            
n = 8
obj = Solution()
print(obj.countBits(n))


0  ,1, 2, 3, 4, 5,
[0, 1, 1, 2, 1, 2]