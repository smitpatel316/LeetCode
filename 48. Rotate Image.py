from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Reverse the list and rotate at symmetry
        matrix.reverse()
        for (i, row) in enumerate(matrix):
            for j in range(i + 1, len(row)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
