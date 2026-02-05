class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        lst = sorted(satisfaction, reverse = True)
        total = 0
        summ = 0
        for i in range(len(lst)):    
            summ += lst[i]        
            if summ < 0:
                break
            total += summ
        
        return total
                
