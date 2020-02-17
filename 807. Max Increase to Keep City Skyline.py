class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        left_to_right = []
        top_to_bottom = []
        prev_size = 0
        for i in range(len(grid)):
            left_to_right.append(max(grid[i]))
            max_val = -1
            for k in range(len(grid)):
                prev_size += grid[i][k]
                if grid[k][i] > max_val:
                    max_val = grid[k][i]
            top_to_bottom.append(max_val)
        new_size = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                left_to_right_max_val = left_to_right[i]
                top_to_bottom_max_val = top_to_bottom[j]
                grid[i][j] = min(left_to_right_max_val, top_to_bottom_max_val)
                new_size += grid[i][j]
        return new_size - prev_size
