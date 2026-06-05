# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count, self.res = 0, 0
        def dfsSearch(root, k):
            if not root:
                return None
            # if self.count == k:
            #     return root.val

            left = dfsSearch(root.left, k)
            self.count += 1
            print(root.val, self.count)
            if self.count == k:
                self.res = root.val
            right = dfsSearch(root.right, k)


        dfsSearch(root, k)
        return self.res
            
                

