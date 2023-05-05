class Solution:
    def minCostII(self, costs) -> int:
        for i in range(len(costs)):
            for j in range(len(costs[i])):
                if i != 0:
                    temp_min = 9999
                    for k in range(len(costs[i-1])):
                        if k != j:
                            temp_min = min(costs[i-1][k],temp_min)
                    costs[i][j] = costs[i][j] + temp_min
        print(map)
        return min(costs[-1])
    
costs = [[17,2,17],[16,16,5],[14,3,19],[11,12,5],[32,4,7]]
obj  = Solution()
print(obj.minCostII(costs))