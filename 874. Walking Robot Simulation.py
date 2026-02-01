class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        obs = set(map(tuple, obstacles))
        n = len(commands)
        x = 0
        y = 0
        maximum = 0
        d = 0
        incre= [(0,1), (1,0), (0,-1), (-1,0)]

        for i in range(n):
            
            if commands[i] == -1:
                d = (d + 1) % 4
            elif commands[i] == -2:
                d = (d - 1) % 4
            else:
                dx, dy = incre[d]
                for _ in range(commands[i]):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in obs:
                        break
                    x, y = nx, ny
            maximum = max(maximum, x**2 + y**2)

        return maximum
