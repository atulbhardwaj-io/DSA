
class Solution(object):
    def longestUnivaluePath(self, root):
        self.ans = 0

        def dfs(root):
            if root is None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            left_path = 0
            right_path = 0

            if root.left and root.left.val == root.val:
                left_path = left + 1

            if root.right and root.right.val == root.val:
                right_path = right + 1

            # Update maximum path using both directions
            self.ans = max(self.ans, left_path + right_path)

            # Return only the longest downward path
            return max(left_path, right_path)

        dfs(root)
        return self.ans