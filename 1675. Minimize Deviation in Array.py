class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        def odd(num: int) -> bool:
            return num % 2 == 1
        
        n = len(nums)

        for i in range(n):
            if odd(nums[i]):
                nums[i] = 2*nums[i]
        
        h = []
        minimum = float('inf')

        for num in nums:
            minimum = min(minimum, num)
            heapq.heappush(h, -num)
        
        result = -h[0] - minimum

        while not odd(-h[0]):
            maximum = -heapq.heappop(h)
            result = min(result, maximum - minimum)
            maximum = maximum // 2
            minimum = min(minimum, maximum)
            heapq.heappush(h, -maximum)

        result = min(-h[0] - minimum, result)

        return result
