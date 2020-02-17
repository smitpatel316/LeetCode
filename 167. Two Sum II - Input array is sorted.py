class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers) < 2:
            return None
        left, right = 0, len(numbers) - 1
        while left < right:
            added = numbers[left] + numbers[right]
            if added == target:
                return [left+1, right+1]
            elif added > target:
                right -= 1
            else:
                left += 1
        return None