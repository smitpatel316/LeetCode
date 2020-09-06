class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        s = str.strip()
        if not s:
            return 0
        is_negative = s[0] == "-"
        if is_negative:
            if len(s) == 1:
                return 0
            s = s[1:]
        if s[0] == "+":
            if is_negative:
                return 0
            if len(s) == 1:
                return 0
            s = s[1:]
        digits = set("0123456789")
        if s[0] not in digits:
            return 0
        for (i, c) in enumerate(s):
            if c not in digits:
                break
        else:
            i = len(s)
        num = int(s[:i])
        if is_negative:
            num = -num
            if num < INT_MIN:
                return INT_MIN
        else:
            if num > INT_MAX:
                return INT_MAX
        return num


if __name__ == "__main__":
    print(Solution().myAtoi("-+1"))
