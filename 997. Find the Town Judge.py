from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust:
            if N == 1:
                return 1
            else:
                return -1
        trusts_other = {}
        trusted_by_other = {}
        for [a, b] in trust:
            if a in trusts_other:
                trusts_other[a].add(b)
            else:
                trusts_other[a] = {b}
            if b not in trusts_other:
                trusts_other[b] = set()
            if b in trusted_by_other:
                trusted_by_other[b].add(a)
            else:
                trusted_by_other[b] = {a}
            if a not in trusted_by_other:
                trusted_by_other[a] = set()

        potential_judge = None
        for b in trusts_other:
            if len(trusts_other[b]) == 0 and len(trusted_by_other[b]) == N - 1:
                potential_judge = b

        if potential_judge:
            return potential_judge
        else:
            return -1


if __name__ == "__main__":
    print(Solution().findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))
