from typing import List


class Solution:
    def fourSumCount(
        self, A: List[int], B: List[int], C: List[int], D: List[int]
    ) -> int:
        a_b_sum = {}
        for (i, a) in enumerate(A):
            for(j, b) in enumerate(B):
                temp_sum = a+b
                if temp_sum not in a_b_sum:
                    a_b_sum[temp_sum] = 1
                else:
                    a_b_sum[temp_sum] += 1

        matches = 0
        for (i, c) in enumerate(C):
            for (j, d) in enumerate(D):
                if -(c+d) in a_b_sum:
                    matches += a_b_sum[-(c+d)]

        return matches