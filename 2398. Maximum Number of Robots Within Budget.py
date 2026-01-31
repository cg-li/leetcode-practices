class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:

        n = len(chargeTimes)
        dq = deque()

        i = 0
        sumrC = 0
        result = 0

        for j in range(n):

            sumrC += runningCosts[j]
            while dq and chargeTimes[dq[-1]] <= chargeTimes[j]:
                dq.pop()
            dq.append(j)            

            while dq and chargeTimes[dq[0]] + ((j-i+1) * sumrC) > budget:
                if dq[0] == i:
                    dq.popleft()
                sumrC -= runningCosts[i]
                i += 1
            result = max(result, j-i+1)

        return result
