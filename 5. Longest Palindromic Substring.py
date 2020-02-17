class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1: return ""

        start, end = 0, 0
        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            len1 = right - left - 1

            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            len2 = right - left - 1

            biggest_len = max(len1, len2)

            if biggest_len > (end - start):
                start = i - int((biggest_len - 1) / 2)
                end = i + int(biggest_len / 2)

        return s[start:end + 1]