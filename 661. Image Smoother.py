from math import floor


class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        new_grey_scale = [[0] * len(M[0]) for _ in M]
        combinations = [
            [-1, -1],
            [-1, 0],
            [-1, 1],
            [0, 1],
            [1, 1],
            [1, 0],
            [1, -1],
            [0, -1],
        ]
        for i in range(len(M)):
            for j in range(len(M[i])):
                numer = M[i][j]
                denom = 1
                for comb in combinations:
                    if 0 <= i + comb[0] < len(M) and 0 <= j + comb[1] < len(M[i]):
                        numer += M[i + comb[0]][j + comb[1]]
                        denom += 1
                new_grey_scale[i][j] = floor(numer / denom)
        return new_grey_scale
