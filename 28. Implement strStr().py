class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        length_of_needle = len(needle)
        for i in range(len(haystack)):
            if (
                    needle[0] == haystack[i]
                    and haystack[i: i + length_of_needle] == needle
            ):
                return i
        return -1
