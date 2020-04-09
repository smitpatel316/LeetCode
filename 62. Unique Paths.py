class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        board = [[0] * m for _ in range(n)]
        for i in range(n):
            board[i][0] = 1
        for i in range(m):
            board[0][i] = 1
        for i in range(1, n):
            for j in range(1, m):
                board[i][j] = board[i - 1][j] + board[i][j - 1]
        return board[n - 1][m - 1]


if __name__ == "__main__":
    print(Solution().uniquePaths(7, 3))
