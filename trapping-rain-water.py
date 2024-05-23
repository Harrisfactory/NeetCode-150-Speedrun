class Solution:
    def trap(self, height: List[int]) -> int:
        
        #two pointer

        #take the min of the pointers
        #loop between the pointers
        #   fill difference if a element is less than min pointer
        #   tabulate difference to total trapped

        #   move min pointer until its larger than prev min
        # else move both pointers until they both change

        l, r = 0, len(height) - 1

        total_trapped = 0

        while l < r:
            if height[l] == 0:
                l+=1
                continue
            if height[r] == 0:
                r-=1
                continue

            lowest_wall = min(height[l], height[r])
            for i in range(l, r):
                #check for cracks to fill
                if height[i] < lowest_wall:
                    #calculate difference to total
                    total_trapped += (lowest_wall-height[i])
                    height[i] = lowest_wall
            height_changed = False
            height_r_prev = height[r]
            height_l_prev = height[l]
            while not height_changed and l < r:
                if height[l] > height_l_prev or height[r] > height_r_prev:
                    break
                if height[l] < height[r]:
                    height_l_prev = height[l]
                    l+=1
                elif height[l] > height[r]:
                    height_r_prev = height[r]
                    r-=1
                else:
                    height_l_prev = height[l]
                    height_r_prev = height[r]
                    l+=1
                    r-=1
        return total_trapped