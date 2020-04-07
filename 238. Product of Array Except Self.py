from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        output[0] = 1
        for i in range(1, len(nums)):
            output[i] = output[i - 1] * nums[i - 1]
        r = 1
        for i in reversed(range(len(nums))):
            output[i] = output[i] * r
            r = r * nums[i]

        return output


if __name__ == "__main__":
    print(Solution().productExceptSelf([1, 2, 3, 4]))
