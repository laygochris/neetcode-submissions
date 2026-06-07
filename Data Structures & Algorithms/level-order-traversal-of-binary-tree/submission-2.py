# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []

        def dfs(root, k):
            if not root:
                return None

            if len(self.res) == k:
                self.res.append([])

            self.res[k].append(root.val)
            dfs(root.left, k + 1)
            dfs(root.right, k + 1)

        dfs(root, 0)
        return self.res

        