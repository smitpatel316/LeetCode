from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        if not A:
            return 0

        if len(A) <= K:
            return len(A)

        l, r = 0, 0
        zero_count = 0
        max_count = 0
        while r < len(A):
            if A[r] == 0:
                zero_count += 1
            if zero_count > K:
                if A[l] == 0:
                    zero_count -= 1
                l += 1
            r += 1
            max_count = max(max_count, r - l)
        return max_count


if __name__ == "__main__":
    print(Solution().longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
    print(
        Solution().longestOnes(
            [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3
        )
    )
