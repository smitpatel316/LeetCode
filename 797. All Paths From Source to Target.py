from typing import List
from collections import deque


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return []
        n = len(graph) - 1
        q = deque([(x, [0, x]) for x in graph[0]])
        paths = []
        while q:
            item = q.popleft()
            val = item[0]
            path = item[1]
            if val == n:
                paths.append(path)
            for i in graph[val]:
                q.append((i, path + [i]))
        return paths


if __name__ == "__main__":
    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    print(Solution().allPathsSourceTarget(graph))
