class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}
        if len(nums) == 1:
            return nums[0]
        for num in nums:
            if num in seen:
                if (seen[num] + 1) > len(nums) / 2:
                    return num
                else:
                    seen[num] += 1
            else:
                seen[num] = 1
