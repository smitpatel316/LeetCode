from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T:
            return []

        if len(T) == 1:
            return [0]

        stack = [0]
        for i in range(1, len(T)):
            while stack and T[i] > T[stack[-1]]:
                T[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)

        while stack:
            T[stack.pop()] = 0

        return T


if __name__ == "__main__":
    print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
