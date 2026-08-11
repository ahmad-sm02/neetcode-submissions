class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        n = len(height)
        total_area = 0

        while l < n - 1:
            l_col = height[l]
            
            # Find the best right boundary:
            # 1. First bar >= l_col
            # 2. Or if none exist, the highest bar to the right
            best_r = l + 1
            max_r_height = -1
            
            for r in range(l + 1, n):
                if height[r] >= l_col:
                    best_r = r
                    break
                if height[r] > max_r_height:
                    max_r_height = height[r]
                    best_r = r

            r_col = height[best_r]
            water_level = min(l_col, r_col)

            # Accumulate water between l and best_r
            for i in range(l + 1, best_r):
                if water_level > height[i]:
                    total_area += water_level - height[i]

            # Jump left pointer directly to the right boundary
            l = best_r

        return total_area