class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:

        m = len(heightMap)
        n = len(heightMap[0])

        pq = []
        water = 0
        visited = [[False] * n for _ in range(m)]
        
        direc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for i in range(m):
            for j in (0, n-1):
                if not visited[i][j]:
                    heapq.heappush(pq, (heightMap[i][j], i, j))
                    visited[i][j] = True

        for j in range(n):
            for i in (0, m-1):
                if not visited[i][j]:
                    heapq.heappush(pq, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        while pq:
            h, i, j = heapq.heappop(pq)
            for di, dj in direc:
                ni = i + di
                nj = j + dj
                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                    nh = heightMap[ni][nj]
                    if nh >= h:
                        heapq.heappush(pq, (nh, ni, nj))
                        visited[ni][nj] = True
                    else:
                        water += h - nh
                        heightMap[ni][nj] = h
                        heapq.heappush(pq, (h, ni, nj))
                        visited[ni][nj] = True
            
        return water
