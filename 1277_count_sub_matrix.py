class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        count = 0

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] ==1:
                    count+=1
                    tempr = r
                    tempc = c
                    while tempr < len(matrix)-1 and tempc < len(matrix[0])-1 and matrix[tempr+1][tempc] ==1 and matrix[tempr][tempc+1] ==1:
                        count+=1
                        tempr+=1
                        tempc+=1

        return count
