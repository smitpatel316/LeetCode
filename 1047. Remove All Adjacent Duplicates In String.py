class Solution:
    def removeDuplicates(self, S: str) -> str:
        if not S:
            return ""
        stack = []
        for i in range(len(S)):
            if not stack or stack[-1][0] != S[i]:
                stack.append([S[i], 1])
            else:
                stack[-1][1] += 1

            if stack[-1][1] >= 2 and (i == len(S) - 1 or S[i + 1] != S[i]):
                if stack[-1][1] % 2 == 0:
                    stack.pop()
                else:
                    stack[-1][1] = 1

        res = ""
        for (c, freq) in stack:
            res += c * freq
        return res
