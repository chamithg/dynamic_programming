class Solution:
    def countSquares(self, matrix):
        count = sum(matrix[0])

        for r in range(1,len(matrix)):
            for c in range(1,len(matrix[0])):
                if matrix[r][c] == 1 and matrix[r-1][c-1] != 0 and matrix[r][c-1] != 0 and matrix[r-1][c] != 0:
                    matrix[r][c] = min(matrix[r-1][c-1],matrix[r][c-1],matrix[r-1][c]) +1

            count += sum(matrix[r])           

        return count
    
matrix =[[0,0,0],
         [0,1,0],
         [0,1,0],
         [1,1,1],
         [1,1,0]]
obj= Solution()
print(obj.countSquares(matrix))