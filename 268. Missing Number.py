from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(1, len(nums) + 1)) - sum(nums)


if __name__ == "__main__":
    test_1 = [3, 0, 1]
    assert Solution().missingNumber(test_1) == 2
    test_2 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    assert Solution().missingNumber(test_2) == 8
