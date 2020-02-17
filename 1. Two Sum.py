class Solution:
    def twoSum(self, nums: "List[int]", target: "int") -> "List[int]":
        seen = {}
        for x in range(len(nums)):
            needed = target - nums[x]
            if needed in seen.keys():
                return [nums.index(needed), x]
            else:
                seen[nums[x]] = True
