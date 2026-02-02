class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:

        n = len(scores)

        d = [[] for _ in range(n)]

        def add(i, nei):
            lst = d[i]
            lst.append(nei)

            lst.sort(key = lambda x: scores[x], reverse = True)
            if len(lst) > 3:
                lst.pop()
        
        for a, b in edges:
            add(a, b)
            add(b, a)

        maximum = -1
                
        for v, w in edges:
            for u in d[v]:
                for x in d[w]:
                    if u != x and u!= w and x != v:
                        maximum = max(maximum, scores[u] + scores[v] + scores[w] + scores[x])
        
        return maximum
