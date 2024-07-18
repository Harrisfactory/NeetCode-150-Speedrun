class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1

        current_minimum = 5001

        while l < r:
            mid = l + (r - l) // 2 #??????
            current_minimum = min(current_minimum, nums[mid])
            
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return min(current_minimum, nums[l])
