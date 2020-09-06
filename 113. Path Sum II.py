# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.paths = []

    def pathSum(self, root: TreeNode, rsum: int):
        if not root:
            return []
        self.helper(root, rsum, [root.val])
        return self.paths

    def helper(self, root, rsum, path):
        if root.val == rsum and root.left is None and root.right is None:
            self.paths.append(path)
            return
        rsum -= root.val
        if root.left is not None:
            self.helper(root.left, rsum, path + [root.left.val])
        if root.right is not None:
            self.helper(root.right, rsum, path + [root.right.val])


if __name__ == "__main__":
    tree = TreeNode(
        5,
        TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
        TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))),
    )
    print(Solution().pathSum(tree, 22))
    print(Solution().pathSum(None, 0))
