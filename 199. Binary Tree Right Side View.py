# Definition for a binary tree node.
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        q = deque([(root, 0)])
        output = []

        while q:
            (node, level) = q.popleft()
            if len(output) < level + 1:
                output.append(node.val)
            else:
                output[level] = node.val

            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        return output


if __name__ == "__main__":
    t = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    print(Solution().rightSideView(t))
