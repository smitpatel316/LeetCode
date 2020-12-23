from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        prev = 0
        curr = 0
        for num in nums:
            temp = prev
            prev = max(curr + num, prev)
            curr = temp
        return prev
