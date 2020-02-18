from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        self.depth_first_search(nums, list(), perms)
        return perms

    def depth_first_search(self, nums, curr_path, perms):
        if not nums:
            perms.append(curr_path)

        for (i, k) in enumerate(nums):
            removed_i = nums[:i] + nums[i + 1 :]
            new_path = curr_path + [k]
            self.depth_first_search(removed_i, new_path, perms)


if __name__ == "__main__":
    print(Solution().permute([1, 2, 3]))
