class Solution:
    def maximalSquare(self, matrix):
        height = len(matrix)
        width = len(matrix[0])
        max_area = 0
        for r in reversed(range(height)):
            for c in reversed(range(width)):
                if r == height-1 or c == width-1:
                    matrix[r][c] = int(matrix[r][c])
                    max_area = max(max_area,matrix[r][c]* matrix[r][c])
                elif matrix[r][c] == "0":
                    matrix[r][c] = 0
                else:
                    if matrix[r][c] == "1":
                        matrix[r][c] = min(matrix [r+1][c],matrix [r+1][c+1],matrix [r][c+1])+1
                        max_area = max(max_area,matrix[r][c]* matrix[r][c])
        return max_area
    
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]   
obj = Solution()
print(obj.maximalSquare(matrix))