# Definition for a binary tree node.
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        q = deque([(root, 0)])
        res = []
        while q:
            data = q.popleft()
            node = data[0]
            val = data[1]

            if len(res) < val + 1:
                res.append([node.val])
            else:
                if val % 2 == 0:
                    res[val].append(node.val)
                else:
                    res[val] = [node.val] + res[val]

            if node.left:
                q.append((node.left, val + 1))
            if node.right:
                q.append((node.right, val + 1))
        return res


if __name__ == "__main__":
    t = TreeNode(
        val=3,
        left=TreeNode(val=9),
        right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=7)),
    )
    print(Solution().zigzagLevelOrder(t))
