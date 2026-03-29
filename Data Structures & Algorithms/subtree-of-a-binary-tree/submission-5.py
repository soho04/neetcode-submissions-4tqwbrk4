# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    
    def sameTree(self, node, subTree):

        if node is None and subTree is None:
            print("here")
            return True

        if node is None or subTree is None or node.val != subTree.val:
            print("here also")
            return False

        return self.sameTree(node.left, subTree.left) and self.sameTree(node.right, subTree.right)

        
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if root and not subRoot:
            return True

        if not root and subRoot:
            return False

        if self.sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5

    #   2
    #  / \
    # 4   5