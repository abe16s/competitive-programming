class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxi = -float("inf")
        while l < r:
            cur = (r-l)*min(height[r],height[l])
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
            maxi = max(maxi, cur)

        return maxi
