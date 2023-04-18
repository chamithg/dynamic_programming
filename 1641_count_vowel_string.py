class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels =["a","e","i","o","u"]

        if n == 1:
            return 5
    

        grid = [[0 for element in range(5)] for element in range(n)]

        for r in range(n):
            for c in range(5):
                if r == 0:
                    grid[r][c] = c+1
                elif c == 0:
                    grid[r][c] = 1
                else:
                    grid[r][c] = grid[r-1][c] + grid[r][c-1]

        return grid[n-1][5-1]
            