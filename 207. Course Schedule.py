from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)

        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visit[i] = 1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


if __name__ == "__main__":
    pre_reqs = [[1, 0]]
    print(Solution().canFinish(2, pre_reqs))
    pre_reqs = [[1, 0], [0, 1]]
    print(Solution().canFinish(2, pre_reqs))
    pre_reqs = [[1, 0], [0, 2], [2, 1]]
    print(Solution().canFinish(3, pre_reqs))
