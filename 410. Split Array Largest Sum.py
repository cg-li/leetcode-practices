class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)

        def feasible(X : int) -> bool:
            part = 1
            current = 0
            for x in nums:
                if current + x <= X:
                    current += x
                else:
                    part += 1
                    current = x
                    if part > k:
                        return False
            return True

        while low < high:
            mid = (low + high) // 2
            if feasible(mid):
                high = mid
            else:
                low = mid + 1

        return high
