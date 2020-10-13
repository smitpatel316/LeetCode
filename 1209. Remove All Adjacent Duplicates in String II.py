class Solution:
    def removeDuplicates(self, S: str, k: int) -> str:
        if not S:
            return ""
        stack = []
        for i in range(len(S)):
            if not stack or stack[-1][0] != S[i]:
                stack.append([S[i], 1])
            else:
                stack[-1][1] += 1

            if stack[-1][1] >= k and (i == len(S) - 1 or S[i + 1] != S[i]):
                if stack[-1][1] % k == 0:
                    stack.pop()
                else:
                    stack[-1][1] = stack[-1][1] % k

        res = ""
        for (c, freq) in stack:
            res += c * freq
        return res
