class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        rev = s[::-1]
        t = s + "#" + rev

        pi = [0] * len(t)

        j = 0

        for i in range(1, len(t)):
            while j > 0 and t[j] != t[i]:
                j = pi[j-1]

            if t[j] == t[i]:
                j += 1
                pi[i] = j
            
        m = pi[-1]
        adding = s[m:][::-1]
        return adding + s
