from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        r = nums[0]
        _max, _min = r, r
        for i in range(1, len(nums)):
            if nums[i] < 0:
                _max, _min = _min, _max
            _max = max(nums[i], _max * nums[i])
            _min = min(nums[i], _min * nums[i])

            r = max(r, _max)
        return r


if __name__ == "__main__":
    print(Solution().maxProduct([-2, 0, -1]))
