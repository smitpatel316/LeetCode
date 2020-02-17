class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2 ** 31 - 1 or x <= -2 ** 31:
            return 0
        x = str(x)
        if x[0] == "-":
            if int("-" + x[:0:-1]) >= 2 ** 31 - 1 or int("-" + x[:0:-1]) <= -2 ** 31:
                return 0
            return int("-" + x[:0:-1])
        else:
            if int(x[::-1]) >= 2 ** 31 - 1 or int(x[::-1]) <= -2 ** 31:
                return 0
            return int(x[::-1])
