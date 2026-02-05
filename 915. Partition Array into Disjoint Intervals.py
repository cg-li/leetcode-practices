class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:

        current = 0
        maxl = nums[0]
        maxr = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= maxl:
                if nums[i] < maxl:
                    maxl = maxr
                    current = i
            elif nums[i] > maxr:
                maxr = nums[i]

        return current+1

"""
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        current = 0
        maxl = nums[0]
        maxr = nums[0]

        for i in range(1, len(nums)):
            maxr = max(maxr, nums[i])
            if nums[i] < maxl:
                current = i
                maxl = maxr

        return current + 1
"""     
