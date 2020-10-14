from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        if len(nums) <= 2:
            return nums
        left = 0
        right = len(nums) - 1
        i = n - 1
        while i > left:
            curr = i
            while curr + 1 < right:
                swap_with = curr + 1
                nums[curr], nums[swap_with] = nums[swap_with], nums[curr]
                curr += 1
            right -= 2
            i -= 1
        return nums


if __name__ == "__main__":
    print(Solution().shuffle([1, 1, 2, 2], 2))
