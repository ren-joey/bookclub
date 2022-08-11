# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def recursive(node):
            if (node is None):
                return 0
            return (node.val if (node.val >= low and node.val <= high) else 0) + recursive(node.left) + recursive(node.right)
        return recursive(root)