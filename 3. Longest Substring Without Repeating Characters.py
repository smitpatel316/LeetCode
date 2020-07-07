class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        result = 1
        for i in range(len(s)):
            checker = True
            seen = {}
            count = 0
            for j in range(i, len(s)):
                if s[j] in seen.keys():
                    break
                else:
                    seen[s[j]] = True
                    count += 1
            if count > result:
                result = count
        return result

    def optimized_solution(self, s):
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
