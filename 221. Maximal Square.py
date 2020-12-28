from collections import defaultdict


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        dp = defaultdict(int)
        max_len = 0
        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[i - 1]) + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[(i, j)] = (
                        min(dp[(i - 1, j)], dp[(i - 1, j - 1)], dp[(i, j - 1)]) + 1
                    )
                    max_len = max(max_len, dp[(i, j)])
        return max_len ** 2
