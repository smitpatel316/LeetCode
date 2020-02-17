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
