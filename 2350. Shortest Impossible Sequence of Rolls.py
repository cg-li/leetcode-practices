class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        
        count = 0
        s = set([])        
        for i in range(len(rolls)):
            if rolls[i] not in s:
                s.add(rolls[i])
            if len(s) == k:
                s = set([])
                count += 1
        return count + 1
