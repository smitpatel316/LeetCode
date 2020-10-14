from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        i = 0
        count = 0
        total = 0
        for j in range(len(nums)):
            if nums[j] % 2 == 1:
                k -= 1
                count = 0
            while k == 0:
                k += int(nums[i] % 2 == 1)
                i += 1
                count += 1
            total += count
        return total


if __name__ == "__main__":
    print(Solution().numberOfSubarrays([1, 1, 2, 1, 1], 3))
