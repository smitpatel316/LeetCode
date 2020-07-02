from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        sub_boxes = [set() for _ in range(9)]

        for (row_i, row) in enumerate(board):
            for (col_i, elem) in enumerate(row):
                if elem != ".":
                    # Row Check
                    if row.count(elem) > 1:
                        return False

                    # Col Check
                    if elem in cols[col_i]:
                        return False
                    else:
                        cols[col_i].add(elem)

                    # Sub Square Check
                    sections = [
                        {"row": range(0, 3), "col": range(0, 3)},
                        {"row": range(0, 3), "col": range(3, 6)},
                        {"row": range(0, 3), "col": range(6, 9)},
                        {"row": range(3, 6), "col": range(0, 3)},
                        {"row": range(3, 6), "col": range(3, 6)},
                        {"row": range(3, 6), "col": range(6, 9)},
                        {"row": range(6, 9), "col": range(0, 3)},
                        {"row": range(6, 9), "col": range(3, 6)},
                        {"row": range(6, 9), "col": range(6, 9)},
                    ]
                    for (i, section) in enumerate(sections):
                        if row_i in section.get("row") and col_i in section.get("col"):
                            if elem in sub_boxes[i]:
                                print("here")
                                return False
                            else:
                                sub_boxes[i].add(elem)
        return True


if __name__ == "__main__":
    sol = Solution()
    # test_1 = [
    #     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    #     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    #     [".", "9", "8", ".", ".", ".", ".", "6", "."],
    #     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    #     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    #     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    #     [".", "6", ".", ".", ".", ".", "2", "8", "."],
    #     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    #     [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    # ]
    # test_1_ans = sol.isValidSudoku(test_1)
    # print(test_1_ans)
    # assert test_1_ans
    #
    # test_2 = [
    #     ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    #     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    #     [".", "9", "8", ".", ".", ".", ".", "6", "."],
    #     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    #     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    #     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    #     [".", "6", ".", ".", ".", ".", "2", "8", "."],
    #     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    #     [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    # ]
    # test_2_ans = sol.isValidSudoku(test_2)
    # print(test_2_ans)
    # assert not test_2_ans

    test_3 = [
        [2, 1, 5, 7, 4, 9, 3, 6, 8],
        [3, 7, 9, 2, 8, 6, 1, 4, 5],
        [4, 8, 6, 3, 1, 5, 9, 7, 2],
        [1, 9, 2, 5, 7, 4, 8, 3, 6],
        [5, 4, 3, 6, 2, 8, 7, 1, 9],
        [7, 6, 8, 1, 9, 3, 2, 5, 4],
        [8, 2, 7, 4, 6, 1, 5, 9, 3],
        [9, 5, 4, 8, 3, 7, 6, 2, 1],
        [6, 3, 1, 9, 5, 2, 4, 8, 7],
    ]
    print(sol.isValidSudoku(test_3))
    # assert not test_3_ans
