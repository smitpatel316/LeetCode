class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if not name or not typed:
            return True

        last_char = 0
        for i in range(len(typed)):
            if last_char < len(name) and name[last_char] == typed[i]:
                last_char += 1
            elif not i or name[last_char - 1] != typed[i]:
                return False

        return last_char == len(name)
