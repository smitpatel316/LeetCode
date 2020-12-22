from typing import List
import math


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not points or not K or len(points) < K:
            return []
        points.sort(key=lambda point: math.sqrt(point[0]**2 + point[1]**2))
        return points[:K]


if __name__ == "__main__":
    print(Solution().kClosest([[3,3],[5,-1],[-2,4]], 2))