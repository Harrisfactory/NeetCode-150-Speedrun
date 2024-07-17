class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        #we want minimum bananas eaten in the total hours taken

        #the absolute minimum bananas we can eat is 1

        #so brute force would be trying the entire range of bananas 1 -> max(piles)

        #so in [3, 6, 7, 11] we have a banana range of 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11

        #I assume we can do a binary search until we r pointer can no longer go left but lets start brute force

        l, r = 1, max(piles)

        result = max(piles)

        #if they cross over we have found our minimum
        while l <= r:
            mid = (l + r) // 2
            #resets every time to check the new mid amount
            hours_taken = 0

            for p in piles:
                hours_taken += math.ceil(float(p) / mid)
            
            #we can move left
            if hours_taken <= h:
                result = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return result

