# 312. Burst Balloons

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        nums = [1] + nums + [1]
        n = len(nums)
        partialsums = [[0]*n for _ in range(0, n)]
        for length in range(2, n):
            for p in range(0, n-length):
                q = p + length
                maximum = 0
                for r in range(p+1, q):
                    s = nums[p] * nums[r] * nums[q]
                    s += partialsums[p][r] + partialsums[r][q]
                    maximum = max(s, maximum)
                partialsums[p][q] = maximum
        return partialsums[0][n-1]
