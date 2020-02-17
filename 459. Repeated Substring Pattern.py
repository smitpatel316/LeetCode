class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        pattern = ""
        for index in range(len(s) // 2 + 1):
            if pattern == "":
                pattern += s[index]
            else:
                if pattern[0] == s[index]:
                    substring = pattern[:index]
                    if (substring * (len(s) // len(substring))) == s:
                        return True
                pattern += s[index]
        return False
