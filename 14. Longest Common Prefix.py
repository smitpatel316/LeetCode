from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]

        prefix = strs[0]

        for i in range(1, len(strs)):
            while (get_index_value(strs[i], prefix) != 0):
                print(prefix)
                prefix = prefix[:len(prefix) - 1]

                if prefix == "":
                    return ""

        return prefix


def get_index_value(string, sub_string):
    try:
        index_value = string.index(sub_string)
    except ValueError:
        index_value = -1
    return index_value