class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = { crs:[] for crs in range(numCourses) }
        res = []
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        visit, cycle = set(), set()
        def dfs(crs):
            if crs in cycle: return False
            if crs in visit: return True
            cycle.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre): return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return []
        return res