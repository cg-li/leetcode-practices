class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        p = k
        q = k
        l1 = 0
        l2 = 0

        result = nums[k]

        t = nums[k]
        n = len(nums)

        while t * n > result:
            while k-l1 >= 0 and nums[k-l1] >= t:
                l1 += 1
            while  k+l2 <= n-1 and nums[k+l2] >= t:
                l2 += 1

            length = l1+l2-1
            result = max(result, length*t)
            if k-l1 == -1 and k+l2 == n:
                break
            else:
                if k-l1 == -1:
                    t = nums[k+l2]
                elif k+l2 == n:
                    t = nums[k-l1]
                else:
                    t = max(nums[k-l1], nums[k+l2])

        return result

