from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda t: t[0])
        new_intervals = [intervals[0]]
        for i in range(1, len(intervals)):
            if new_intervals[-1][0] <= intervals[i][0] <= new_intervals[-1][1]:
                new_intervals[-1][1] = max(intervals[i][1], new_intervals[-1][1])
            else:
                new_intervals.append(intervals[i])
        return new_intervals


if __name__ == "__main__":
    print(Solution().merge([[1, 4], [0, 2], [3, 5]]))
    print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
