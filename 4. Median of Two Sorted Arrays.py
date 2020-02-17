from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = nums1 + nums2
        total.sort()
        index = int(len(total) / 2)
        if len(total) % 2 == 0:
            return float(total[index] + total[index - 1]) / 2
        else:
            return float(total[index])
