from typing import List


class Solution:
    """
    If a mine ('M') is revealed, then the game is over - change it to 'X'.
    If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
    If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
    Return the board when no more squares will be revealed.
    """

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        [row, col] = click
        if board[row][col] == "M":
            board[row][col] = "X"
            return board
        elif board[row][col] == "E":
            mines = self.adjacent_mines(board, row, col)
            if mines:
                board[row][col] = str(mines)
            else:
                board[row][col] = "B"
                directions = [
                    (-1, -1),
                    (-1, 0),
                    (-1, 1),
                    (0, -1),
                    (0, 1),
                    (1, 1),
                    (1, 0),
                    (1, -1),
                ]
                is_safe = lambda row_i, col_i: 0 <= row_i < len(
                    board
                ) and 0 <= col_i < len(board[row_i])
                for i, j in directions:
                    if is_safe(row + i, col + j) and board[row + i][col + j] == "E":
                        board = self.updateBoard(board, [row + i, col + j])
        return board

    @staticmethod
    def adjacent_mines(board, row, col):
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
        ]
        mines = 0
        is_safe = lambda row_i, col_i: 0 <= row_i < len(board) and 0 <= col_i < len(
            board[row_i]
        )
        for i, j in directions:
            if is_safe(row + i, col + j) and board[row + i][col + j] == "M":
                mines += 1
        return mines


if __name__ == "__main__":
    b = [
        ["E", "E", "E", "E", "E"],
        ["E", "E", "M", "E", "E"],
        ["E", "E", "E", "E", "E"],
        ["E", "E", "E", "E", "E"],
    ]
    from pprint import pprint

    pprint(Solution().updateBoard(b, [3, 0]))
