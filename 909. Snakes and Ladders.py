from typing import List
import math
from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        goal = n * n
        if not board:
            return -1

        q = deque([1])
        dist = {1: 0}
        while q:
            position = q.popleft()
            if position == goal:
                return dist[position]
            for i in range(position + 1, min(position + 6, goal) + 1):
                (row, col) = self.get_position(i, n)
                if board[row][col] != -1:
                    i = board[row][col]
                if i not in dist:
                    dist[i] = dist[position] + 1
                    q.append(i)
        return -1

    def get_position(self, position, n):
        quotient, remainder = divmod(position - 1, n)
        row = n - 1 - quotient
        col = remainder if row % 2 != n % 2 else n - 1 - remainder
        return row, col


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.snakesAndLadders(
            [
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, 35, -1, -1, 13, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, 15, -1, -1, -1, -1],
            ]
        )
    )
