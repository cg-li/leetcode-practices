class Solution(object):
    def countPalindromicSubsequences(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        M = 10**9 + 7
        n = len(s)

        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        prevsame = [-1] * n
        last = {}
        for i, ch in enumerate(s):
            prevsame[i] = last.get(ch, -1)
            last[ch] = i
        
        nextsame = [n] * n
        last = {}
        for i in range(n-1, -1, -1):
            ch = s[i]
            nextsame[i] = last.get(ch, n)
            last[ch] = i

        for l in range(1, n):
            for i in range(n-l):
                j = i + l
                if s[i] != s[j]:
                    dp[i][j] = (dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]) % M
                else:
                    low = nextsame[i]
                    high = prevsame[j]
                    if low < high:
                            dp[i][j] = (2*dp[i+1][j-1] - dp[low+1][high-1]) % M
                    elif low == high:
                            dp[i][j] = (2*dp[i+1][j-1] + 1) % M
                    else:
                        dp[i][j] = (2*dp[i+1][j-1] +2) % M
            
        return dp[0][n-1]
