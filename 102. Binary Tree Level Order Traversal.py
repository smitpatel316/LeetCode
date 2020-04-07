# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue = [[root, 0]]
        levels = []
        while len(queue) > 0:
            queue_item = queue.pop(0)
            node = queue_item[0]
            level = queue_item[1]
            if len(levels) == level:
                levels.append([node.val])
            else:
                levels[level].append(node.val)
            if node.left is not None:
                queue.append([node.left, level + 1])
            if node.right is not None:
                queue.append([node.right, level + 1])

        return levels


if __name__ == "__main__":
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)
    Solution().levelOrder(tree)