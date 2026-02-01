class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:

        n = len(flowers)
        m = len(people)

        start = sorted(s for s, e in flowers)
        end = sorted(e for s, e in flowers)

        enumeration = sorted((time, i) for i, time in enumerate(people))
        result = [0] * m

        j = 0
        k = 0

        for time, i in enumeration:
            while j < n and start[j] <= time:
                j += 1
            while k < n and end[k] < time:
                k += 1
            result[i] = j - k

        return result 
