from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_val = -1
        min_val_index = None
        slots = []
        for num in nums:
            if len(slots) == 0:
                slots.append(num)
                min_val = num
                min_val_index = 0
            elif len(slots) < k:
                if num < min_val:
                    min_val = num
                    min_val_index = len(slots)
                slots.append(num)
            else:
                if num > min_val:
                    slots.pop(min_val_index)
                    slots.append(num)
                    min_val = min(slots)
                    min_val_index = slots.index(min_val)

        return min_val


if __name__ == "__main__":
    Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)
    Solution().findKthLargest([4, 5, 6, 3, 2, 3, 1, 5, 2, ], 4)
