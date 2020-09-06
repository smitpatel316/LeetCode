import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = [(matrix[0][0], 0, 0)]
        res = -1
        for _ in range(k):
            res, i, j = heapq.heappop(heap)
            if j == 0 and i + 1 < n:
                heapq.heappush(heap, (matrix[i + 1][j], i + 1, j))
            if j + 1 < n:
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
        return res


if __name__ == "__main__":
    print(Solution().kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
