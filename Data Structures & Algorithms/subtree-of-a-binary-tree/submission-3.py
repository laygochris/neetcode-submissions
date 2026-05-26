# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False

        if self.sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))

    def sameTree(self, r, sR):
        if not r and not sR:
            return True

        if (r and sR) and (r.val == sR.val):
            return (self.sameTree(r.left, sR.left) and
                    self.sameTree(r.right, sR.right))
        return False