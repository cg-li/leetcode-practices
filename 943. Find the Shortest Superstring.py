class Solution(object):
    def shortestSuperstring(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
        n = len(words)

        def overlapcount(i,j):
            wordA = words[i]
            wordB = words[j]
            for k in range(min(len(wordA), len(wordB)), 0, -1):
                if wordA[-k:] == wordB[:k]:
                    return k
            else: return 0

        overlap = [[0]*n for _ in range(n)]
        add = [[0]*n for _ in range(n)]
        append = [[""]*n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i == j:
                     continue
                k = overlapcount(i,j)
                overlap[i][j] = k
                append[i][j] = words[j][k:]
                add[i][j] = len(words[j]) - k

        
        INF = 10**9
        dp = [[INF]*n for _ in range(1<<n)]
        parent = [[-1]*n for _ in range(1<<n)]
        for j in range(n):
            dp[1<<j][j] = len(words[j])


        for mask in range(1 << n):
            for last in range(n):
                if dp[mask][last] == INF: continue
                for nxt in range(n):
                    if mask & (1<<nxt):
                        continue
                    newmask  = mask | (1<<nxt)
                    newlength = dp[mask][last] + add[last][nxt]
                    if newlength < dp[newmask][nxt]:
                        dp[newmask][nxt] = newlength
                        parent[newmask][nxt] = last


        full = (1<<n) - 1 
        last = min(range(n), key = lambda j: dp[full][j])

        lst = []
        mask = full
        while last != -1:
            lst.append(last)
            prev = parent[mask][last]
            mask ^= (1<<last)
            last = prev
        lst.reverse()

        result = words[lst[0]]
        for p, q in zip(lst, lst[1:]):
            result += append[p][q]
        
        return result
