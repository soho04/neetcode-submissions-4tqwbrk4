# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        bfs_queue = deque([root]) 
        right_side_view = []

        while bfs_queue:

            level = []

            for _ in range(len(bfs_queue)):

                node = bfs_queue.popleft()

                if node.left:
                    bfs_queue.append(node.left)

                if node.right:
                    bfs_queue.append(node.right)

            right_side_view.append(node.val)

        return right_side_view