from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        max_rows = len(board)
        max_cols = len(board[0])
        for (row_i, row) in enumerate(board):
            for (col_i, elem) in enumerate(row):
                neighbors = [
                    (-1, -1),
                    (-1, 0),
                    (-1, 1),
                    (0, -1),
                    (0, 1),
                    (1, -1),
                    (1, 0),
                    (1, 1),
                ]
                total_alive = 0
                for neighbor in neighbors:
                    neighbor_coordinate = (row_i + neighbor[0], col_i + neighbor[1])
                    if (
                        0 <= neighbor_coordinate[0] < max_rows
                        and 0 <= neighbor_coordinate[1] < max_cols
                    ):
                        neighbor_state = board[neighbor_coordinate[0]][
                            neighbor_coordinate[1]
                        ]
                        if neighbor_state in [-1, 1]:
                            total_alive += 1

                if (total_alive < 2 or total_alive > 3) and elem == 1:
                    board[row_i][col_i] = -1
                elif total_alive == 3 and elem == 0:
                    board[row_i][col_i] = 2

        for (row_i, row) in enumerate(board):
            for (col_i, elem) in enumerate(row):
                if elem == 2:
                    board[row_i][col_i] = 1
                elif elem == -1:
                    board[row_i][col_i] = 0


if __name__ == "__main__":
    inp = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    Solution().gameOfLife(inp)
