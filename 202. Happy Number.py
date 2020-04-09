class Solution:
    def __init__(self):
        self.seen = []

    def isHappy(self, n: int) -> bool:
        square_sum = 0
        while True:
            for ch in str(n):
                square_sum += (int(ch) ** 2)
            if square_sum == 1:
                return True
            elif square_sum in self.seen:
                return False
            else:
                self.seen.append(square_sum)
                return self.isHappy(square_sum)


if __name__ == "__main__":
    print(Solution().isHappy(19))
