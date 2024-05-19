import numpy

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        nums_copy = list(nums)
        seen_nums = {}

        for i in range(len(nums)):
            if nums[i] in seen_nums:
                nums_copy[i] = seen_nums[nums[i]]
                continue
            left_product = numpy.prod(nums[0:i])
            right_product = numpy.prod(nums[i+1:])
            nums_copy[i] = int(left_product * right_product)
            seen_nums[nums[i]] = nums_copy[i]
        
        return nums_copy
