class Solution:
    def numOfWays(self, n: int) -> int:
        M = 10 ** 9 + 7
        dp = {}
        for i in range(1,4):
            for j in range(1,4):
                for k in range(1,4):
                    if j!= i and k!=j:
                        dp[(i,j,k)] = 1
        
        for s in range(2, n+1):
            newdp = defaultdict(int)
            for i in range(1,4):
                for j in range(1,4):
                    for k in range(1,4):
                        if j!=i and k!=j:
                            for p in range(1,4):
                                for q in range(1,4):
                                    for r in range(1,4):
                                        if p!=q and q!=r:
                                            if p!=i and q!=j and r!=k:
                                                newdp[(i,j,k)] += dp[(p,q,r)]
                                                newdp[(i,j,k)] %= M
            dp = newdp

        result = 0
        for key in dp:
            result += dp[key]
            result %= M
        
        return result
