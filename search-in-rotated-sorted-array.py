class Solution:
    def search(self, nums: List[int], target: int) -> int:

        #a bit better than brute force approach
        #l, r = 0, len(nums) - 1

        #while l <= r:
        #    mid = (l + r) // 2

        #    if nums[mid] == target:
        #        return mid
        #    elif target in nums[mid+1:]:
        #        l = mid + 1
        #    else:
        #        r = mid - 1
        #return -1
        
        #even better, see if we can simply check if each side is sorted
        l, r = 0, len(nums) -1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[l] <= nums[mid] and target >= nums[l] and target <= nums[mid]:
                r = mid - 1
            elif nums[r] <= nums[mid] and target >= nums[r] and target <= nums[mid]:
                l = mid + 1
            elif target in nums[mid+1:]:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1
