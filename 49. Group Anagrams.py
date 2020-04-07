from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for string in strs:
            string_sorted = "".join(sorted(string))
            if string_sorted in seen:
                seen[string_sorted].append(string)
            else:
                seen[string_sorted] = [string]
        return list(seen.values())


if __name__ == "__main__":
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
