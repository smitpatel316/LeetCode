from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        freq = {}
        for num in nums1:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        res = []
        for num in nums2:
            if num in freq and freq[num] > 0:
                res.append(num)
                freq[num] -= 1

        return res


if __name__ == "__main__":
    Solution().intersect([4, 9, 5], [9, 4, 9, 8, 4])
