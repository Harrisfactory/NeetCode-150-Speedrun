class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_water = 0

        l, r = 0, len(height) - 1

        while l < r:
            #need the minimum for our calculation so water doesnt spill
            min_height = min(height[l], height[r])
            max_water = max(max_water, (r-l)*min_height)
            if height[l] < height[r]:
                l+=1
            elif height[l] > height[r]:
                r-=1
            else:
                l+=1
                r-=1

        return max_water