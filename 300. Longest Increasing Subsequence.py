from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []
        max_len = 0
        for i, num in enumerate(nums):
            if not stack or stack[-1] < num:
                stack.append(num)
                max_len = max(max_len, len(stack))
            elif stack[-1] > num:
                while stack and stack[-1] > num:
                    stack.pop()
                stack.append(num)
        return max_len


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(sol.lengthOfLIS([3, 4, 3, 1, 1]))
    print(sol.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))
