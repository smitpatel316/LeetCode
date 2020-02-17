from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = -1
        while left < right:
            temp_area = (right - left) * min(height[left], height[right])
            if temp_area > max_area:
                max_area = temp_area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
