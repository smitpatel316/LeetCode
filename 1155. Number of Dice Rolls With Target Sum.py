class Solution:
    def __init__(self):
        self.memo = {}

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if d == 0:
            return 0 if target > 0 else 1

        if (d, target) in self.memo:
            return self.memo[(d, target)]

        total = 0
        for i in range(max(0, target - f), target):
            total += self.numRollsToTarget(d - 1, f, i)
        total %= 10 ** 9 + 7
        self.memo[(d, target)] = total
        return total
