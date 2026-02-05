class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        pro = []
        n = len(profits)
        
        cap = []
        for i in range(n):
            heapq.heappush(cap, (capital[i], i))

        m = 0
        w0 = w
        while m < k:
            while cap and cap[0][0] <= w:
                c, i = heapq.heappop(cap)
                heapq.heappush(pro, (-profits[i], i))
            if not pro:
                break
            p, j = heapq.heappop(pro)
            p = -p
            w += p
            m += 1
        return w
            
