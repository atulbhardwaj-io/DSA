
from collections import defaultdict, deque

class Solution(object):
    def verticalTraversal(self, root):
        if root is None:
            return []

        nodes = defaultdict(lambda: defaultdict(list))
        que = deque()

        que.append((root, (0, 0)))

        while que:
            p = que.popleft()

            node = p[0]
            x = p[1][0]
            y = p[1][1]

            nodes[x][y].append(node.val)

            if node.left:
                que.append((node.left, (x - 1, y + 1)))

            if node.right:
                que.append((node.right, (x + 1, y + 1)))

        ans = []

        for x in sorted(nodes.keys()):
            col = []

            for y in sorted(nodes[x].keys()):
                col.extend(sorted(nodes[x][y]))

            ans.append(col)

        return ans
