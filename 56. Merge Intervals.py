from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        i = 1
        while i < len(intervals):
            _interval = intervals[i]
            _before = intervals[i - 1]
            if _before[0] <= _interval[0] <= _before[1]:
                intervals[i - 1][1] = max(_interval[1], _before[1])
                intervals.pop(i)
                i -= 1
            i += 1
        return intervals


if __name__ == "__main__":
    print(Solution().merge([[1, 4], [0, 2], [3, 5]]))
    print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
