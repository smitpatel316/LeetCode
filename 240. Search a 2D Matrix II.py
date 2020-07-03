class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        if len(matrix) == 1 and len(matrix[0]) == 1 and matrix[0][0] == target:
            return True

        mid_row = len(matrix) // 2
        mid_col = len(matrix[0]) // 2
        if matrix[mid_row][mid_col] == target:
            return True
        if matrix[mid_row][mid_col] < target:
            matrix_below = []
            if mid_row + 1 != len(matrix):
                matrix_below = [matrix[i] for i in range(mid_row + 1, len(matrix))]

            matrix_right = []
            for i in range(mid_row + 1):
                row = []
                for j in range(mid_col + 1, len(matrix[0])):
                    row.append(matrix[i][j])
                matrix_right.append(row)

            return self.searchMatrix(matrix_below, target) or self.searchMatrix(
                matrix_right, target
            )
        else:
            matrix_above = [matrix[i] for i in range(mid_row)]

            matrix_left = []
            for i in range(mid_row, len(matrix)):
                row = []
                for j in range(mid_col):
                    row.append(matrix[i][j])
                matrix_left.append(row)

            return self.searchMatrix(matrix_above, target) or self.searchMatrix(
                matrix_left, target
            )


if __name__ == "__main__":
    print(
        Solution().searchMatrix(
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ],
            5,
        )
    )
