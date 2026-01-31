class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        dp = [0] * n

        for i in range(n):
            dp[i] = i
        
        def expand(l, c):
            while l >= 0 and c < n and s[c] == s[l]:
                if l == 0:
                    dp[c] = 0
                else:
                    dp[c] = min(dp[c], dp[l-1]+1)
                l -= 1
                c += 1
                
        for i in range(n):
            expand(i,i)
            expand(i, i+1)
        
        return dp[-1]
            
