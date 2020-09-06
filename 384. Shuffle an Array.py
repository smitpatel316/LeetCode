import random
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.init_nums = list(nums)
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.init_nums
        self.init_nums = list(self.init_nums)
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        if len(self.nums) > 0:
            for (i, num) in enumerate(self.nums):
                index = random.randrange(i, len(self.nums))
                self.nums[i], self.nums[index] = self.nums[index], self.nums[i]
        return self.nums


if __name__ == "__main__":
    a = Solution([1, 2, 3])

    for _ in range(10):
        print(a.shuffle())
    print(a.reset())
