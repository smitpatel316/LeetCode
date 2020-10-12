
class Solution:
    def minimumTotal(self, triangle):
        f = [0] * (len(triangle) + 1)
        for row in triangle[::-1]:
            for i in range(len(row)):
                f[i] = row[i] + min(f[i], f[i + 1])
        return f[0]


if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
    print(sol.minimumTotal(
[[-1],[2,3],[1,-1,-3]]))
