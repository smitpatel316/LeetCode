from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int):
        index = self.binary_search(nums, 0, len(nums) - 1, target)
        if (
            index == -1
            or len(nums) == 1
            or (index == 0 and nums[index + 1] != target)
            or (index == len(nums) - 1 and nums[index - 1] != target)
        ):
            return [index, index]

        left, right = index, index
        while left - 1 >= 0 and nums[left - 1] == target:
            left -= 1
        while right + 1 < len(nums) and nums[right + 1] == target:
            right += 1
        return [left, right]

    def binary_search(self, nums, left, right, target):
        if right < left:
            return -1
        mid = (right + left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binary_search(nums, left, mid - 1, target)
        else:
            return self.binary_search(nums, mid + 1, right, target)


if __name__ == "__main__":
    print(Solution().searchRange([1, 2, 2, 3, 4, 4, 5], 7))
