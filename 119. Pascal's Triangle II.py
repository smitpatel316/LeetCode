from math import factorial


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return [combination(rowIndex, i) for i in range(rowIndex + 1)]


def combination(n, k):
    # n = row
    # k = pos
    return int(factorial(n) / (factorial(k) * factorial(n - k)))