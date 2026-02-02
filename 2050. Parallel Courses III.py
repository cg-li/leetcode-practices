class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        
        dp = time[:]
        graph = defaultdict(list)

        indeg = [0] * n

        for u, v in relations:
            u -= 1
            v -= 1
            graph[u].append(v)
            indeg[v] += 1

        q = deque()

        for i in range(n):
            if indeg[i] == 0:
                q.append(i)

        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v in graph[u]:
                indeg[v] -= 1
                dp[v] = max(dp[u] + time[v], dp[v])
                if indeg[v] == 0:
                    q.append(v)
        
        return max(dp)
