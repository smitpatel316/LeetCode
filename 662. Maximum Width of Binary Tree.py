from collections import deque, namedtuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        levels = {}
        NodeWrapper = namedtuple("NodeWrapper", ["node", "level", "pos"])
        q = deque([NodeWrapper(root, 0, 1)])
        max_width = 0
        while q:
            node = q.popleft()
            if node.level not in levels:
                levels[node.level] = [node.pos, node.pos]

            levels[node.level][0] = min(levels[node.level][0], node.pos)
            levels[node.level][1] = max(levels[node.level][1], node.pos)
            max_width = max(
                max_width, abs(levels[node.level][1] - levels[node.level][0])
            )

            if node.node.left:
                q.append(NodeWrapper(node.node.left, node.level + 1, node.pos * 2 - 1))
            if node.node.right:
                q.append(NodeWrapper(node.node.right, node.level + 1, node.pos * 2))

        return max_width + 1
