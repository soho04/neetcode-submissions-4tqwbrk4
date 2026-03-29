# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return

        bfs_queue = deque([root])

        while bfs_queue:

            node = bfs_queue.popleft()
            node.left, node.right = node.right, node.left

            if node.left:
                bfs_queue.append(node.left)
            if node.right:
                bfs_queue.append(node.right)


        return root
    
    # [1, 3, 2]

            


        