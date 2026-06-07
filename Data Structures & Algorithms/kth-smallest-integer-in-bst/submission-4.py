class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.res = None

        def dfs(node):
            if not node:
                return False # Keep searching
            
            # 1. Search Left
            if dfs(node.left): 
                return True # Found it! Stop everything.
            
            # 2. Visit Current
            self.count += 1
            if self.count == k:
                self.res = node.val
                return True # Found it!
            
            # 3. Search Right
            return dfs(node.right)

        dfs(root)
        return self.res