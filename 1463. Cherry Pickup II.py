class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m = len(grid)
        n = len(grid[0])

        dp = [[float("-inf")] * n for _ in range(n)]
        dp[0][n-1] = grid[0][0] + (grid[0][n-1] if n-1 != 0 else 0)

        for i in range(1, m):
            newdp = [[float("-inf")]*n for _ in range(n)]
            for p in range(0, n):
                for q in range(0, n):
                    value = float("-inf")
                    for s in (p-1, p, p+1):
                        if 0<=s<n:
                            for t in (q-1, q, q+1):
                                if 0<=t<n:
                                    value = max(dp[s][t], value)
                    if value == float("-inf"): continue
                    if p == q:
                        newdp[p][q] = value + grid[i][p]
                    else:
                        newdp[p][q] = value + grid[i][p] + grid[i][q]
            dp = newdp
        
        result = 0

        for i in range(n):
            for j in range(n):
                result = max(result, dp[i][j])

        
        return result
