class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 0:
            return 0
        perfect_squares = [float("inf")] * (n + 1)
        perfect_squares[0] = 0
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                perfect_squares[i] = min(
                    perfect_squares[i], perfect_squares[i - j * j] + 1
                )
                j += 1

        return int(perfect_squares[n])


if __name__ == "__main__":
    print(Solution().numSquares(12))
