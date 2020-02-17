import itertools
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        t, n, z, p = [], {}, 0, {}  # triplet, negative, zero, positive
        for i in nums:
            if i < 0:
                if i not in n:
                    n[i] = 0
                n[i] += 1
            elif i > 0:
                if i not in p:
                    p[i] = 0
                p[i] += 1
            else:
                z += 1
        if z >= 3:
            t.append((0, 0, 0))
        if len(n) > 0 and len(p) > 0:
            if z > 0:
                for i in n:
                    k = -i
                    if k in p:
                        t.append((i, 0, k))
            for i, j in itertools.combinations_with_replacement(n.keys(), 2):
                if i == j and n[i] < 2:
                    continue
                k = -(i + j)
                if k in p:
                    t.append((i, j, k))
            for j, k in itertools.combinations_with_replacement(p.keys(), 2):
                if j == k and p[j] < 2:
                    continue
                i = -(j + k)
                if i in n:
                    t.append((i, j, k))
        return t