class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:

        n = len(grid)

        if n == 1:
            return grid[0][0]

        INF = 10 **9
        dp = [INF] * n

        for i in range(n):
            dp[i] = grid[0][i]
        
        for i in range(1, n):
            min1 = INF
            min2 = INF

            m = -1

            for j, value in enumerate(dp):
                if value < min1:
                    min2 = min1
                    min1 = value
                    m = j
                elif value < min2:
                    min2 = value
            
            new = [0] * n
            for j in range(n):
                prev = min1 if j != m else min2
                new[j] = prev + grid[i][j]
            dp = new

        return min(dp)
