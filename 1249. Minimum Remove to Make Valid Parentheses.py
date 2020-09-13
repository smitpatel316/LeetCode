class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return s
        stack = []
        i = 0
        while i < len(s):
            if s[i] == "(":
                stack.append(i)
            if s[i] == ")":
                if len(stack) == 0:
                    s = s[:i] + s[i+1:]
                    i -= 1
                else:
                    stack.pop()
            i += 1
        counter = 0
        for i in stack:
            s = s[:(i-counter)] + s[(i+1-counter):]
            counter += 1
        return s

if __name__ == "__main__":
    print(Solution().minRemoveToMakeValid("lee(t(c)o)de)"))
    print(Solution().minRemoveToMakeValid("a)b(c)d"))
    print(Solution().minRemoveToMakeValid("))(("))
    print(Solution().minRemoveToMakeValid("(a(b(c)d)"))