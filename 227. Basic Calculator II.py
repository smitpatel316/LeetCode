class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        curr_num = 0
        curr_opp = "+"
        stack = []
        for i in range(len(s)):
            if s[i].isdigit():
                curr_num = curr_num * 10 + (ord(s[i]) - ord("0"))
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s) - 1:
                if curr_opp == "-":
                    stack.append(-curr_num)
                elif curr_opp == "+":
                    stack.append(curr_num)
                elif curr_opp == "*":
                    stack.append(stack.pop() * curr_num)
                else:
                    tmp = stack.pop()
                    if tmp // curr_num < 0 and tmp % curr_num != 0:
                        stack.append(tmp // curr_num + 1)
                    else:
                        stack.append(tmp // curr_num)
                curr_opp = s[i]
                curr_num = 0
        return sum(stack)
