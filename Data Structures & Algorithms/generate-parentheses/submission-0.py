class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # count of ( and ) is == to lenght n return that posibilitie
        # ( if count of ( < lenght n
        # ) if count of ) < count (
        stack = []
        res = []
        def dfs(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
            
            if openN < n:
                stack.append('(')
                dfs(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(')')
                dfs(openN, closedN + 1)
                stack.pop()
        dfs(0, 0)
        return res