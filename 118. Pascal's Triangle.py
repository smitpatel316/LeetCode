from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        triangle = [[1]]
        for num_row in range(2, numRows + 1):
            row = []
            for i in range(num_row):
                if i - 1 < 0 or i >= len(triangle):
                    row.append(1)
                else:
                    row.append(triangle[num_row - 2][i - 1] + triangle[num_row - 2][i])
            triangle.append(row)
        return triangle


if __name__ == "__main__":
    print(Solution().generate(2))
