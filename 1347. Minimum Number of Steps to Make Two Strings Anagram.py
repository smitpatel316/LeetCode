from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        if s == t:
            return 0
        c1 = Counter(s)
        c2 = Counter(t)
        if c1 == c2:
            return 0
        for c in c2:
            if c in c1:
                if c1[c] == c2[c]:
                    c1[c] = 0
                    c2[c] = 0
                elif c1[c] < c2[c]:
                    c2[c] -= c1[c]
                    c1[c] = 0
                else:
                    c1[c] -= c2[c]
                    c2[c] = 0
        return sum(c2.values())
