class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        if not matrix or not matrix[0]:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        path = [[0] * n for _ in range(m)]

        def validneighbor(i,j):
            result = []
            if i-1 >= 0:
                if matrix[i-1][j] > matrix[i][j]:
                    result.append((i-1, j))
            if j-1 >= 0:
                if matrix[i][j-1] > matrix[i][j]:
                    result.append((i, j-1))
            if i+1 <= m-1:
                if matrix[i+1][j] > matrix[i][j]:
                    result.append((i+1, j))
            if j+1 <= n-1:
                if matrix[i][j+1] > matrix[i][j]:
                    result.append((i, j+1))
            return result       


        def dfs(i,j):
            if path[i][j] != 0:
                return path[i][j]
            else:
                l = 1
                for p,q in validneighbor(i,j):
                    l = max(l, dfs(p,q)+1)

                path[i][j] = l
                return path[i][j]

        maxpath = 0
        for i in range(m):
            for j in range(n):
                maxpath = max(maxpath, dfs(i,j))

        return maxpath
