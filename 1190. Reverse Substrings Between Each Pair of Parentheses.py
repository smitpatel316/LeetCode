class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        i = 0

        while i < len(s):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                start = stack.pop()
                _reversed = s[start + 1 : i][::-1]
                s = s[:start] + _reversed + s[i + 1 :]
                i -= 2

            i += 1
        return s


if __name__ == "__main__":
    print(Solution().reverseParentheses("(abcd)"))
    print(Solution().reverseParentheses("(u(love)i)"))
    print(Solution().reverseParentheses("(ed(et(oc))el)"))
    print(Solution().reverseParentheses("a(bcdefghijkl(mno)p)q"))
