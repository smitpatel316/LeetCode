from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1
        output = []
        while r1 <= r2 and c1 <= c2:
            for i in range(c1, c2 + 1):
                output.append(matrix[r1][i])
            for i in range(r1 + 1, r2 + 1):
                output.append(matrix[i][c2])
            if r1 < r2 and c1 < c2:
                for i in range(c2 - 1, c1, -1):
                    output.append(matrix[r2][i])
                for i in range(r2, r1, -1):
                    output.append(matrix[i][c1])
            r1 += 1
            r2 -= 1
            c1 += 1
            c2 -= 1
        return output


if __name__ == "__main__":
    print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
    print(
        Solution().spiralOrder(
            [
                [1, 1, 1, 1, 1, 1, 1],
                [1, 2, 2, 2, 2, 2, 1],
                [1, 2, 3, 3, 3, 2, 1],
                [1, 2, 2, 2, 2, 2, 1],
                [1, 1, 1, 1, 1, 1, 1],
            ]
        )
    )
