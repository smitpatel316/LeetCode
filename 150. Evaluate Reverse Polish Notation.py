from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        stack = []
        for token in tokens:
            if token.isdigit() or (token[0] == "-" and token[1:].isdigit()):
                stack.append(int(token))
            elif token == "+":
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                stack.append(operand_1 + operand_2)
            elif token == "-":
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                stack.append(operand_1 - operand_2)
            elif token == "*":
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                stack.append(operand_1 * operand_2)
            elif token == "/":
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                stack.append(int(float(operand_1) / operand_2))
        return stack[-1]


if __name__ == "__main__":
    print(
        Solution().evalRPN(
            ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        )
    )
