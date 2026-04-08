class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        Bellman Ford Algorithm
        Where n is the number of cities, m is the number of flights and 
        k is the number of stops.
        Time: O(n + (m * k))
        Space: O(n)
        """
        prices = [float("inf")] * n
        prices[src] = 0
        for i in range(k + 1):
            tmpPrices = prices.copy()
            for s, d, p in flights:
                if prices[s] == float("inf"): continue
                if prices[s] + p < tmpPrices[d]: tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return prices[dst] if prices[dst] != float("inf") else -1