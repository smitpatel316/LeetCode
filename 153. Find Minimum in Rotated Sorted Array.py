from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif mid - 1 >= 0 and nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid - 1
