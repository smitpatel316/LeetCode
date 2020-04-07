from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        runner1 = nums[0]
        runner2 = nums[0]
        while True:
            runner1 = nums[runner1]
            runner2 = nums[nums[runner2]]
            if runner1 == runner2:
                break

        p1 = nums[0]
        p2 = runner1
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]
        return p1
