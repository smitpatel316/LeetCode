class Solution:
    def intToRoman(self, num: int) -> str:
        symbol = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        edge_cases = {4: "IV", 9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM"}
        res = ""
        for i in [1000, 500, 100, 50, 10, 5, 1]:
            if not num:
                break
            str_num = str(num)
            if str_num[0] in ["9", "4"]:
                _num = int(str_num[0]) * (10 ** (len(str_num) - 1))
                res += edge_cases[_num]
                num -= _num
            quotient, remainder = divmod(num, i)
            res += quotient * symbol[i]
            num = remainder
        return res


if __name__ == "__main__":
    sol = Solution()
    for test, res in [
        (2, "II"),
        (12, "XII"),
        (27, "XXVII"),
        (4, "IV"),
        (3, "III"),
        (9, "IX"),
        (58, "LVIII"),
        (1994, "MCMXCIV"),
    ]:
        print(sol.intToRoman(test) == res)
