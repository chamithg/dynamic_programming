class Solution:
    def trap(self, height):
        
        len_arr = len(height)
        left = 0
        left_pos = 0
        trapped_water = 0
        high_lands = 0
        dp = [0]* len_arr
        for i in range(len_arr):
            if height[i] > 0:
                if left == 0:
                    left = height[i]
                    left_pos = i+1
                else:
                    if height[i] <= left:
                        high_lands += height[i]
                    else:
                        trapped_water += (left * (i-(left_pos)) -high_lands)
                        left = height[i]
                        left_pos = i+1
                        high_lands = 0
                    
        return trapped_water

height= [0,1,0,2,1,0,1,3,2,1,2,1]        
obj = Solution()
print(obj.trap(height))
        