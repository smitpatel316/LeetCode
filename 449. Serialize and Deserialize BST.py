from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        values = []
        # Pre Order
        def dfs(root):
            if root:
                values.append(root.val)
                dfs(root.left)
                dfs(root.right)

        dfs(root)
        return " ".join(map(str, values))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        values = deque(map(int, data.split(" ")))

        def build(min_val, max_val):
            if values and min_val < values[0] < max_val:
                value = values.popleft()
                node = TreeNode(value)
                node.left = build(min_val, value)
                node.right = build(value, max_val)
                return node

        return build(float("-inf"), float("inf"))


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
