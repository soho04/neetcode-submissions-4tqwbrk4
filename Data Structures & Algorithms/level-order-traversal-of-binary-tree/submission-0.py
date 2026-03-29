# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        bfs_queue = deque([root])
        res = [[root.val]]

        while bfs_queue:

            level = []

            for _ in range(len(bfs_queue)):

                node = bfs_queue.popleft()

                if node.left:
                    bfs_queue.append(node.left)
                    level.append(node.left.val)
                if node.right:
                    bfs_queue.append(node.right)
                    level.append(node.right.val)

            if level:
                res.append(level)

        return res


        # 1, 2, 3, 4, 5, 6, 7

        # [1 ]

        # []