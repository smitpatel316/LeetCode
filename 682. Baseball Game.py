class Solution:
    def calPoints(self, ops: List[str]) -> int:
        sum = 0
        valid_rounds = []
        for (index, op) in enumerate(ops):
            if op == "C":
                sum -= valid_rounds.pop()
            elif op == "D":
                sum += valid_rounds[-1] * 2
                valid_rounds.append(valid_rounds[-1] * 2)
            elif op == "+" and len(valid_rounds) >= 2:
                sum += valid_rounds[-2] + valid_rounds[-1]
                valid_rounds.append(valid_rounds[-2] + valid_rounds[-1])
            else:
                valid_rounds.append(int(op))
                sum += int(op)
        return sum
