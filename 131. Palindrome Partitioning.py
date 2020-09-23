from typing import List


class Solution:
    def __init__(self):
        self.seen = {}

    def partition(self, s: str) -> List[List[str]]:
        if s in self.seen:
            return self.seen[s]
        if not s:
            return [[]]

        if len(s) == 1:
            return [[s]]
        else:
            result = []
            for i in range(len(s)):
                if s[: i + 1] == s[: i + 1][::-1]:
                    for comb in self.partition(s[i + 1 :]):
                        result.append([s[: i + 1]] + comb)
            self.seen[s] = result
            return result


if __name__ == "__main__":
    print(Solution().partition("aab"))
