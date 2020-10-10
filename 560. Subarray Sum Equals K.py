from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        left = 0
        right = 0
        sub_array_sum = 0
        curr_sum = nums[0]
        while len(nums) > right >= left:
            if curr_sum == k:
                sub_array_sum += 1
                right += 1
                if right < len(nums):
                    curr_sum += nums[right]
            elif curr_sum > k:
                curr_sum -= nums[left]
                left += 1
            else:
                right += 1
                if right < len(nums):
                    curr_sum += nums[right]
        return sub_array_sum


if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraySum([2, 1, 1, 1], 2))
