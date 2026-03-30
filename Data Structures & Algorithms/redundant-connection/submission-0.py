class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)   # hashmap para lista de adyacencia
        
        # Construcción del grafo
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = {}               # hashmap para visitados
        cycle = set()
        cycleStart = -1

        def dfs(node, parent):
            nonlocal cycleStart

            if visit.get(node, False):
                cycleStart = node
                return True

            visit[node] = True

            for nei in adj[node]:
                if nei == parent:
                    continue

                if dfs(nei, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if node == cycleStart:
                        cycleStart = -1
                    return True

            return False

        # Puede empezar desde cualquier nodo presente
        dfs(edges[0][0], -1)

        # Buscar la última arista que conecta dos nodos del ciclo
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]