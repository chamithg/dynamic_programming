class Solution:
    def calculateMinimumHP(self, dungeon):
        height = len(dungeon)
        width = len(dungeon[0])
        
        out = [[0 for col in range(width)] for row in range(height)]
        for r in reversed(range(height)):
            for c in reversed(range(width)):
                if r == height-1 and c == width-1:
                    if dungeon[r][c] >= 1:
                        out[r][c] = 1
                    else:
                        out[r][c] = abs(dungeon[r][c]) +1
                elif r == height-1:
                    if dungeon[r][c] >= out[r][c+1]:
                        out[r][c] = 1
                    else:
                        out[r][c] = out[r][c+1] - dungeon[r][c] 
                elif c == width-1:
                    if dungeon[r][c] >= out[r+1][c]:
                        out[r][c] = 1
                    else:
                        out[r][c] = out[r+1][c] - dungeon[r][c]         
                else:
                    if dungeon[r][c] < 1:
                        out[r][c] = min(out[r+1][c],out[r][c+1])+ abs(dungeon[r][c])
                    else:
                        out[r][c] = max(min(out[r+1][c],out[r][c+1])- dungeon[r][c],1)
        return out[0][0]
        
        

dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
obj = Solution()
print(obj.calculateMinimumHP(dungeon))