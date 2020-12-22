class Solution:
    def longestPalindrome(self, s: str) -> str:
        # if len(s) < 1:
        #     return ""
        #
        # start, end = 0, 0
        # for i in range(len(s)):
        #     left, right = i, i
        #     while left >= 0 and right < len(s) and s[left] == s[right]:
        #         left -= 1
        #         right += 1
        #     len1 = right - left - 1
        #
        #     left, right = i, i + 1
        #     while left >= 0 and right < len(s) and s[left] == s[right]:
        #         left -= 1
        #         right += 1
        #
        #     len2 = right - left - 1
        #
        #     biggest_len = max(len1, len2)
        #
        #     if biggest_len > (end - start):
        #         start = i - int((biggest_len - 1) / 2)
        #         end = i + int(biggest_len / 2)
        #
        # return s[start : end + 1]

        # DP Solution

        if not s:
            return ""
        dp = {}
        res = None
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                dp[(i, j)] = (j - i < 3 or dp[(i + 1, j - 1)]) and s[i] == s[j]
                if dp[(i, j)] and (res is None or j - i + 1 > len(res)):
                    res = s[i : j + 1]
        return res


if __name__ == "__main__":
    print(Solution().longestPalindrome("ac"))
