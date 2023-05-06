class Solution:
    def minCost(self, costs):

        map = [[0 for i in range(3)] for j in range(len(costs))]
        for i in range(len(costs)):
            for j in range(3):
                if i == 0:
                    map[i][j] = costs[i][j]
                elif j == 0:
                    map[i][j] = costs[i][j] + min(map[i-1][1],map[i-1][2])
                elif j == 1:
                    map[i][j] = costs[i][j] + min(map[i-1][0],map[i-1][2])
                elif j == 2:
                    map[i][j] = costs[i][j] + min(map[i-1][1],map[i-1][0])   
        return min(map[-1])
                
costs = [[17,2,17],[16,16,5],[14,3,19],[11,12,5],[32,4,7]]
obj  = Solution()
print(obj.minCost(costs))