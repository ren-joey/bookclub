class Solution:
    cur_sum = 0

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        stack = [root]
        cur_sum = 0

        while stack:
            node = stack.pop()

            if not node:
                continue

            if node.val > low:
                stack.append(node.left)

            if node.val < high:
                stack.append(node.right)

            if low <= node.val <= high:
                cur_sum += node.val

        return cur_sum