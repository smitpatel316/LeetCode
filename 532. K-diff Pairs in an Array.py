class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        seen = {}
        if k < 0:
            return 0
        for (i, num) in enumerate(nums):
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        counter = 0
        for key in seen.keys():
            if k == 0:
                if seen[key] > 1:
                    counter += 1
            else:
                if (key + k) in seen:
                    counter += 1
        return counter
