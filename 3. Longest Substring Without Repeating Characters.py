class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        max_length = 0
        seen = set()
        while left <= right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
                max_length = max(max_length, right - left)
            else:
                seen.remove(s[left])
                left += 1
        return max_length

    def optimized_solution(self, s):
        ans = 0
        seen = {}
        i, j = 0, 0
        while j < len(s):
            if s[j] in seen:
                i = max(seen[s[j]], i)
            ans = max(ans, j - i + 1)
            seen[s[j]] = j + 1
            j += 1
        return ans
