class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL = maxR = 0
        res = 0
        while l < r:
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])
            if maxL <= maxR:
                waterL = maxL - height[l]
                res += 0 if waterL < 0 else waterL
                l += 1
            else:
                waterR = maxR - height[r]
                res += 0 if waterR < 0 else waterR
                r -= 1
        return res