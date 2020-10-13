# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        positive_levels = []
        negative_levels = [None]
        q = deque([[root, (0, 0)]])
        while q:
            node, (x, y) = q.popleft()
            if x < 0:
                tmp_x = x * -1
                if len(negative_levels) - 1 < tmp_x:
                    negative_levels.append([[node.val, y]])
                else:
                    negative_levels[tmp_x].append([node.val, y])
            else:
                if len(positive_levels) - 1 < x:
                    positive_levels.append([[node.val, y]])
                else:
                    positive_levels[x].append([node.val, y])
            if node.left:
                q.append([node.left, (x - 1, y - 1)])
            if node.right:
                q.append([node.right, (x + 1, y - 1)])
        negative_levels = negative_levels[1:][::-1]
        for i, level in enumerate(negative_levels):
            level.sort(key=lambda x: (x[1] * -1, x[0]))
            vals = [x for (x, _) in level]
            negative_levels[i] = vals
        for i, level in enumerate(positive_levels):
            level.sort(key=lambda x: (x[1] * -1, x[0]))
            vals = [x for (x, _) in level]
            positive_levels[i] = vals
        return negative_levels + positive_levels


if __name__ == "__main__":
    t = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(Solution().verticalTraversal(t))
