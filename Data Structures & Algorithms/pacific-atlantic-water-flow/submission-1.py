class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(i, j, visited):
            visited.add((i, j))
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if (0 <= ni < m and 0 <= nj < n
                        and (ni, nj) not in visited
                        and heights[ni][nj] >= heights[i][j]):
                    dfs(ni, nj, visited)

        for i in range(m):
            dfs(i, 0, pacific)        # bord gauche
            dfs(i, n - 1, atlantic)   # bord droit
        for j in range(n):
            dfs(0, j, pacific)        # bord haut
            dfs(m - 1, j, atlantic)   # bord bas

        return [[i, j] for (i, j) in pacific & atlantic]

        