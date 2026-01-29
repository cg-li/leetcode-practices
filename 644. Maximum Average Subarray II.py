class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        low = float(min(nums))
        high = float(max(nums))
        n = len(nums)

        epsilon = 1e-5


        while high - low > epsilon:
            X = (low + high)/2.0
            P = [0.0] * (n+1)
            for i in range(1, n+1):
                P[i] = P[i-1] + nums[i-1] - X

            minimum = 0.0
            valid = False

            for i in range(k, n+1):
                minimum = min(P[i-k], minimum)
                if P[i] - minimum >= 0:
                    valid = True
                    break
            if valid:
                low = X
            else:
                high = X
        
        return low
