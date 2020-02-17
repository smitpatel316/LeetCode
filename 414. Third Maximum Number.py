class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Store max, second_max, and third_max
        max = float("-inf")
        second_max = float("-inf")
        third_max = float("-inf")
        for num in nums:
            if num > max:
                third_max = second_max
                second_max = max
                max = num
            elif second_max < num < max:
                third_max = second_max
                second_max = num
            elif third_max < num < second_max:
                third_max = num

        if third_max != float("-inf"):
            return third_max
        else:
            return max
