class Solution(object):
    def decodeString(self, s):
        stack = []
        curr_num = 0
        curr_string = ""
        for c in s:
            if c == "[":
                stack.append(curr_string)
                stack.append(curr_num)
                curr_string = ""
                curr_num = 0
            elif c == "]":
                num = stack.pop()
                prev_string = stack.pop()
                curr_string = prev_string + num * curr_string
            elif c.isdigit():
                curr_num = curr_num * 10 + int(c)
            else:
                curr_string += c
        return curr_string


if __name__ == "__main__":
    sol = Solution()
    print(sol.decodeString("3[a]2[bc]") == "aaabcbc")
    print(sol.decodeString("3[a2[c]]") == "accaccacc")
    print(sol.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef")
    print(sol.decodeString("abc3[cd]xyz") == "abccdcdcdxyz")
