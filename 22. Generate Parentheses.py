from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        perms = []
        self.backtrack(n, "", 0, 0, perms)
        return perms

    def backtrack(self, n, str, left, right, perms):
        if len(str) == 2 * n:
            perms.append(str)
        else:
            if left < n:
                self.backtrack(n, str + "(", left + 1, right, perms)
            if right < left:
                self.backtrack(n, str + ")", left, right + 1, perms)


if __name__ == "__main__":
    print(Solution().generateParenthesis(3))
