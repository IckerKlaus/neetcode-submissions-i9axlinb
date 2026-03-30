class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges: return 0
        adj = {i:[] for i in range(n)}
        for edg1, edg2 in edges:
            adj[edg1].append(edg2)
            adj[edg2].append(edg1)
        
        visit = set()
        def dfs(node):
            for nei in adj[node]:
                if not nei in visit:
                    visit.add(nei)
                    dfs(nei)
        
        res = 0
        for node in range(n):
            if node not in visit:
                visit.add(node)
                dfs(node)
                res += 1
        return res