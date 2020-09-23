from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        left = 0
        right = len(nums) - 1
        i = 0
        while i < len(nums) and left < right:
            if nums[i] == 0:
                if i >= left:
                    nums[i], nums[left] = nums[left], nums[i]
                    left += 1
                else:
                    i += 1
            elif nums[i] == 2:
                if i <= right:
                    nums[i], nums[right] = nums[right], nums[i]
                    right -= 1
                else:
                    i += 1
            else:
                i += 1


if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    s = Solution()
    s.sortColors(nums)
    print(nums)
    nums = [2, 0, 1]
    s.sortColors(nums)
    print(nums)
    nums = [0]
    s.sortColors(nums)
    print(nums)
