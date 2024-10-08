class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[float('inf')] * n for _ in range(n)]

        def f(i: int, j: int) -> int:
            if i == n - 1:
                return triangle[i][j]
            if dp[i][j] != float('inf'):
                return dp[i][j]
            down = triangle[i][j] + f(i + 1, j)
            diag = triangle[i][j] + f(i + 1, j + 1)
            dp[i][j] = min(down, diag)
            return dp[i][j]

        return f(0, 0)
