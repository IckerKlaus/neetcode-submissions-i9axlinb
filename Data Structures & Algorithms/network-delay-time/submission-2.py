class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Dijkstra's Algorithm
        Time: O(E*logV)
        Space: O(V + E)
        """
        adj = {i: [] for i in range(1, n + 1)}
        
        for u, v, w in times:
            adj[u].append((w, v)) # (weigh, neighbor)

        shortest = {}
        minHeap = [(0, k)] # (weigth, node)
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest: continue
            shortest[n1] = w1
            t = w1
            for w, nb in adj[n1]:
                if nb not in shortest: heapq.heappush(minHeap, (w1 + w, nb))
        return t if len(shortest) == n else -1