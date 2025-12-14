class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        dq = deque()
        n = len(nums)
        result = []
        for i in range(0,n):
            if dq and dq[0] <= i - k:
                dq.popleft()
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            if i >= k-1:
                result.append(nums[dq[0]])
        return result
