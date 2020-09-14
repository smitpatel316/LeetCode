class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        invalid = 0
        for c in s:
            if c == "(":
                stack.append("(")
            elif c == ")":
                if len(stack) == 0:
                    invalid += 1
                else:
                    stack.pop()
        return invalid + len(stack)


if __name__ == "__main__":
    test_cases = ["())", "(((", "()", "()))(("]
    answers = [1, 3, 0, 4]
    sol = Solution()

    for i, case in enumerate(test_cases):
        print(sol.minAddToMakeValid(case) == answers[i])
