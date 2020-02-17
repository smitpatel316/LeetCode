import math


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        for (index, value) in enumerate(s):
            if index + 1 < len(s) and roman_to_int.get(value) < roman_to_int.get(
                s[index + 1]
            ):
                total -= roman_to_int.get(value)
            else:
                total += roman_to_int.get(value)
        return total
