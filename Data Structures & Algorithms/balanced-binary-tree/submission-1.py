# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):

            if not node:
                return 0

            leftHeight = dfs(node.left)
            if leftHeight == -1:
                return -1
            rightHeight = dfs(node.right)
            if rightHeight == -1:
                return -1
            if abs(leftHeight - rightHeight) > 1:
                return -1

            return 1 + max(dfs(node.left), dfs(node.right))
        
        return dfs(root) != -1
            

        #       1 
        #      / \
        #     2   2
        #    /     \
        #   3       3
        #  /         \
        # 4           4