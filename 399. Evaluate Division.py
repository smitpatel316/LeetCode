from typing import List
from collections import deque


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = {}
        for ([i, j], val) in zip(equations, values):
            if i not in graph:
                graph[i] = {}
            if j not in graph:
                graph[j] = {}
            graph[i][j] = val
            graph[j][i] = 0 if val == 0 else 1 / val
        result = []
        for i, j in queries:
            q = deque([[i, 1]])
            visited = {i}
            found = False
            while q and not found:
                (node, total) = q.popleft()
                if node in graph:
                    for _next in graph[node]:
                        if _next == j:
                            result.append(total * graph[node][_next])
                            found = True
                            break
                        elif _next not in visited:
                            q.append([_next, total * graph[node][_next]])
                            visited.add(_next)
            if not found:
                result.append(-1)
        return result


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.calcEquation(
            [["a", "b"], ["b", "c"]],
            [2, 3],
            [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
        )
    )
    print(
        sol.calcEquation(
            equations=[["a", "b"], ["b", "c"], ["bc", "cd"]],
            values=[1.5, 2.5, 5.0],
            queries=[["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
        )
    )
    print(
        sol.calcEquation(
            equations=[["a", "b"]],
            values=[0.5],
            queries=[["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]],
        )
    )
    print(
        sol.calcEquation(
            [["a", "e"], ["b", "e"]], [4.0, 3.0], [["a", "b"], ["e", "e"], ["x", "x"]]
        )
    )
