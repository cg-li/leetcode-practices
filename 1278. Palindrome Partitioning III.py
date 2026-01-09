class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        cost = [[0]*n for _ in range(n)]
        for i in range(0, n):
            for j in range(i, n):
                p, q = i, j
                while p < q:
                    if s[p] != s[q]:
                        cost[i][j] += 1
                    p += 1
                    q -= 1
        
        INF = 10 ** 9
        dp = [[INF]*n for _ in range(k+1)]
        for end in range(n):
            dp[1][end] = cost[0][end]

        for i in range(2, k+1):
            for j in range(i-1, n):
                best = INF
                for prevend in range(i-2, j):
                    best = min(best, dp[i-1][prevend] + cost[prevend+1][j])
                dp[i][j] = best

        return dp[k][n-1]

