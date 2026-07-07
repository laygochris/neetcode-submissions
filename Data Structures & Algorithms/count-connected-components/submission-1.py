class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        trees = 0
        adj = {i:[] for i in range(n)}
        visited = set()

        for p, c in edges:
            adj[p].append(c)
            adj[c].append(p)

        def dfs(n):
            for c in adj[n]:
                if c not in visited:
                    visited.add(c)
                    dfs(c)
        

        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                trees += 1
            

        return trees
