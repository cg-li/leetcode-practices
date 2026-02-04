class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        n = len(grid)
        
        pq = [(grid[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]

        direc = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while pq:
            cost, x, y = heapq.heappop(pq)
            if visited[x][y]:
                continue
            visited[x][y] = True

            if x == n-1 and y == n-1:
                return cost
            
            for dx, dy in direc:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    nc = max(grid[nx][ny], cost)
                    heapq.heappush(pq, (nc, nx, ny))
