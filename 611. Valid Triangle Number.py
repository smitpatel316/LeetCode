from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        count = 0
        nums.sort()
        for i in range(len(nums) - 2):
            k = i + 2
            for j in range(i + 1, len(nums) - 1):
                if nums[i] == 0:
                    break
                while k < len(nums) and nums[i] + nums[j] > nums[k]:
                    k += 1
                count += k - j - 1
        return count


if __name__ == "__main__":
    print(Solution().triangleNumber([2, 5, 6, 7, 9]))
