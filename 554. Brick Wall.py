from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        if not wall or not wall[0]:
            return 0
        gaps = {}
        max_gap = 0
        for i in range(len(wall)):
            for j in range(len(wall[i]) - 1):
                if j != 0:
                    wall[i][j] += wall[i][j - 1]
                if wall[i][j] not in gaps:
                    gaps[wall[i][j]] = 0
                gaps[wall[i][j]] += 1
                if gaps[wall[i][j]] > max_gap:
                    max_gap = gaps[wall[i][j]]
        return len(wall) - max_gap


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.leastBricks(
            [[1, 2, 2, 1], [3, 2, 1], [1, 4, 1], [2, 4], [3, 1, 2], [1, 3, 2]]
        )
    )
    print(sol.leastBricks([[1], [1], [1]]))
