# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        result = []
        final = []
        que = deque([[root, 0]])
        visit = []

        if root is None:
            return []

        while que:
            node = que.popleft()

            if node[1] not in visit:
                visit.append(node[1])
                result.append(node)
                final.append([node[0].val])

            else:
                final[node[1]].append(node[0].val)

            if node[0].left:
                que.append([node[0].left, node[1] + 1])

            if node[0].right:
                que.append([node[0].right, node[1] + 1])

        return final